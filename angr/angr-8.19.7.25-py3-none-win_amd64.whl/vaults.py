import collections
import contextlib
import tempfile
import weakref
import logging
import claripy
import pickle
import shelve
import uuid
import os
import io

l = logging.getLogger("angr.vault")

class VaultPickler(pickle.Pickler):
    def __init__(self, vault, file, *args, assigned_objects=(), **kwargs):
        """
        A persistence-aware pickler.
        It will check for persistence of any objects except for those with IDs in 'assigned_objects'.
        """

        super().__init__(file, *args, **kwargs)
        self.vault = vault
        self.assigned_objects = assigned_objects

    def persistent_id(self, obj):
        if any(obj is o for o in self.assigned_objects):
            return None

        pid = self.vault._get_persistent_id(obj)
        if pid is None:
            return None

        l.debug("Persistent store: %s %s", obj, pid)
        return self.vault.store(obj, id=pid)

class VaultUnpickler(pickle.Unpickler):
    def __init__(self, vault, file, *args, **kwargs):
        super().__init__(file, *args, **kwargs)
        self.vault = vault

    def persistent_load(self, pid):
        return self.vault.load(pid)

class Vault(collections.MutableMapping):
    """
    The vault is a serializer for angr.
    """

    #
    # These MUST be overriden.
    #

    def _read_context(self, i):
        """
        Should be a context that yields a pickle-read()able file object for the given id i.
        """
        raise NotImplementedError()

    def _write_context(self, i):
        """
        Should be a context that yields a pickle-write()able file object for the given id i.
        """
        raise NotImplementedError()

    def keys(self):
        """
        Should return the IDs stored by the vault.
        """
        raise NotImplementedError()

    #
    # Persistance managers
    #

    def __init__(self):
        self._object_cache = weakref.WeakValueDictionary()
        self._uuid_cache = weakref.WeakKeyDictionary()
        self.stored = set()
        self.storing = set()
        self.hash_dedup = {
            claripy.ast.Base, claripy.ast.BV, claripy.ast.FP, claripy.ast.Bool, claripy.ast.Int, claripy.ast.Bits,
        }
        self.module_dedup = set() # {'claripy', 'angr', 'archinfo', 'pyvex' } # cle causes recursion
        self.uuid_dedup = { SimState, Project }
        self.unsafe_key_baseclasses = {
            claripy.ast.Base, SimType
        }

    def _get_persistent_id(self, o):
        """
        Determines a persistent ID for an object.
        Does NOT do stores.
        """
        if type(o) in self.hash_dedup:
            oid = o.__class__.__name__ + "-" + str(hash(o))
            self._object_cache[oid] = o
            return oid

        if any(isinstance(o,c) for c in self.unsafe_key_baseclasses):
            return None

        try:
            return self._uuid_cache[o]
        except KeyError:
            pass
        except TypeError:
            return None

        #if type(o) in self.uuid_dedup:
        #    return self._get_id(o)
        if o.__class__.__module__.split('.')[0] in self.module_dedup or o.__class__ in self.uuid_dedup:
            oid = o.__class__.__name__.split(".")[-1] + '-' + str(uuid.uuid4())
            self._object_cache[oid] = o
            self._uuid_cache[o] = oid
            return oid

        return None

    #
    # Other stuff
    #

    def is_stored(self, i):
        """
        Checks if the provided id is already in the vault.
        """
        if i in self.stored:
            return True

        try:
            with self._read_context(i):
                return True
        except (AngrVaultError, EOFError):
            return False

    def load(self, id): #pylint:disable=redefined-builtin
        """
        Retrieves one object from the pickler with the provided id.

        :param id: an ID to use
        """
        l.debug("LOAD: %s", id)
        try:
            l.debug("... trying cached")
            return self._object_cache[id]
        except KeyError:
            l.debug("... cached failed")
            with self._read_context(id) as u:
                return VaultUnpickler(self, u).load()

    def store(self, o, id=None): #pylint:disable=redefined-builtin
        """
        Stores an object and returns its ID.

        :param o: the object
        :param id: an ID to use
        """
        actual_id = id or self._get_persistent_id(o) or "TMP-"+str(uuid.uuid4())

        l.debug("STORE: %s %s", o, actual_id)

        # this handles recursive objects
        if actual_id in self.storing:
            return actual_id

        if self.is_stored(actual_id):
            l.debug("... already stored")
            return actual_id

        with self._write_context(actual_id) as output:
            self.storing.add(actual_id)
            VaultPickler(self, output, assigned_objects=(o,)).dump(o)
            self.stored.add(actual_id)

        return actual_id

    def dumps(self, o):
        """
        Returns a serialized string representing the object, post-deduplication.

        :param o: the object
        """
        f = io.BytesIO()
        VaultPickler(self, f).dump(o)
        f.seek(0)
        return f.read()

    def loads(self, s):
        """
        Deserializes a string representation of the object.

        :param s: the string
        """
        f = io.BytesIO(s)
        return VaultUnpickler(self, f).load()

    @staticmethod
    def close():
        pass

    #
    # For MutableMapping.
    #

    def __setitem__(self, k, v):
        self.store(v, id=k)

    def __getitem__(self, k):
        return self.load(k)

    def __delitem__(self, k):
        raise AngrVaultError("We currently don't support deletion from the vault.")

    def __iter__(self):
        return iter(self.keys())

    def __len__(self):
        return len(self.keys())

class VaultDict(Vault):
    """
    A Vault that uses a dictionary for storage.
    """
    def __init__(self, d=None):
        super().__init__()
        self._dict = { } if d is None else d

    @contextlib.contextmanager
    def _write_context(self, i):
        f = io.BytesIO()
        yield f
        f.seek(0)
        self._dict[i] = f.read()

    @contextlib.contextmanager
    def _read_context(self, i):
        try:
            f = io.BytesIO(self._dict[i])
            yield f
        except KeyError as e:
            raise AngrVaultError from e

    def is_stored(self, i):
        return i in self._dict

    def keys(self):
        return self._dict.keys()

class VaultDir(Vault):
    """
    A Vault that uses a directory for storage.
    """
    def __init__(self, d=None):
        super().__init__()
        self._dir = tempfile.mkdtemp() if d is None else d
        with contextlib.suppress(FileExistsError):
            os.makedirs(self._dir)

    @contextlib.contextmanager
    def _write_context(self, i):
        with open(os.path.join(self._dir, i), "wb") as o:
            yield o

    @contextlib.contextmanager
    def _read_context(self, i):
        try:
            with open(os.path.join(self._dir, i), "rb") as o:
                yield o
        except FileNotFoundError as e:
            raise AngrVaultError from e

    def keys(self):
        return os.listdir(self._dir)

class VaultShelf(VaultDict):
    """
    A Vault that uses a shelve.Shelf for storage.
    """
    def __init__(self, path=None):
        self._path = tempfile.mktemp() if path is None else path
        s = shelve.open(self._path, protocol=-1)
        super().__init__(s)

    def close(self):
        self._dict.close()

from .errors import AngrVaultError
from .project import Project
from .sim_type import SimType
from .sim_state import SimState
