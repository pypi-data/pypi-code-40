#!/usr/bin/env python

from __future__ import print_function

import atexit
import os
import sys
import re
import gc
import heapq
import locale
import shutil
import time
import unittest
import doctest
import operator
import subprocess
import tempfile
import traceback
import warnings
import zlib
import glob
from contextlib import contextmanager

try:
    import platform
    IS_PYPY = platform.python_implementation() == 'PyPy'
    IS_CPYTHON = platform.python_implementation() == 'CPython'
except (ImportError, AttributeError):
    IS_CPYTHON = True
    IS_PYPY = False

from io import open as io_open
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO  # doesn't accept 'str' in Py2

try:
    import cPickle as pickle
except ImportError:
    import pickle

try:
    import threading
except ImportError: # No threads, no problems
    threading = None

try:
    from collections import defaultdict
except ImportError:
    class defaultdict(object):
        def __init__(self, default_factory=lambda : None):
            self._dict = {}
            self.default_factory = default_factory
        def __getitem__(self, key):
            if key not in self._dict:
                self._dict[key] = self.default_factory()
            return self._dict[key]
        def __setitem__(self, key, value):
            self._dict[key] = value
        def __contains__(self, key):
            return key in self._dict
        def __repr__(self):
            return repr(self._dict)
        def __nonzero__(self):
            return bool(self._dict)

try:
    from unittest import SkipTest
except ImportError:
    class SkipTest(Exception):  # don't raise, only provided to allow except-ing it!
        pass
    def skip_test(reason):
        sys.stderr.write("Skipping test: %s\n" % reason)
else:
    def skip_test(reason):
        raise SkipTest(reason)

try:
    basestring
except NameError:
    basestring = str

WITH_CYTHON = True
CY3_DIR = None

from distutils.command.build_ext import build_ext as _build_ext
from distutils import sysconfig
from distutils import ccompiler
_to_clean = []

@atexit.register
def _cleanup_files():
    """
    This is only used on Cygwin to clean up shared libraries that are unsafe
    to delete while the test suite is running.
    """

    for filename in _to_clean:
        if os.path.isdir(filename):
            shutil.rmtree(filename, ignore_errors=True)
        else:
            try:
                os.remove(filename)
            except OSError:
                pass


def get_distutils_distro(_cache=[]):
    if _cache:
        return _cache[0]
    # late import to accommodate for setuptools override
    from distutils.dist import Distribution
    distutils_distro = Distribution()

    if sys.platform == 'win32':
        # TODO: Figure out why this hackery (see http://thread.gmane.org/gmane.comp.python.cython.devel/8280/).
        config_files = distutils_distro.find_config_files()
        try:
            config_files.remove('setup.cfg')
        except ValueError:
            pass
        distutils_distro.parse_config_files(config_files)

        cfgfiles = distutils_distro.find_config_files()
        try:
            cfgfiles.remove('setup.cfg')
        except ValueError:
            pass
        distutils_distro.parse_config_files(cfgfiles)
    _cache.append(distutils_distro)
    return distutils_distro


EXT_DEP_MODULES = {
    'tag:numpy':     'numpy',
    'tag:numpy_old': 'numpy',
    'tag:pythran':  'pythran',
    'tag:setuptools':  'setuptools.sandbox',
    'tag:asyncio':  'asyncio',
    'tag:pstats':   'pstats',
    'tag:posix':    'posix',
    'tag:array':    'array',
    'tag:coverage': 'Cython.Coverage',
    'Coverage':     'Cython.Coverage',
    'tag:ipython':  'IPython.testing.globalipapp',
    'tag:jedi':     'jedi_BROKEN_AND_DISABLED',
    'tag:test.support': 'test.support',  # support module for CPython unit tests
}

def patch_inspect_isfunction():
    import inspect
    orig_isfunction = inspect.isfunction
    def isfunction(obj):
        return orig_isfunction(obj) or type(obj).__name__ == 'cython_function_or_method'
    isfunction._orig_isfunction = orig_isfunction
    inspect.isfunction = isfunction

def unpatch_inspect_isfunction():
    import inspect
    try:
        orig_isfunction = inspect.isfunction._orig_isfunction
    except AttributeError:
        pass
    else:
        inspect.isfunction = orig_isfunction

def def_to_cdef(source):
    '''
    Converts the module-level def methods into cdef methods, i.e.

        @decorator
        def foo([args]):
            """
            [tests]
            """
            [body]

    becomes

        def foo([args]):
            """
            [tests]
            """
            return foo_c([args])

        cdef foo_c([args]):
            [body]
    '''
    output = []
    skip = False
    def_node = re.compile(r'def (\w+)\(([^()*]*)\):').match
    lines = iter(source.split('\n'))
    for line in lines:
        if not line.strip():
            output.append(line)
            continue

        if skip:
            if line[0] != ' ':
                skip = False
            else:
                continue

        if line[0] == '@':
            skip = True
            continue

        m = def_node(line)
        if m:
            name = m.group(1)
            args = m.group(2)
            if args:
                args_no_types = ", ".join(arg.split()[-1] for arg in args.split(','))
            else:
                args_no_types = ""
            output.append("def %s(%s):" % (name, args_no_types))
            line = next(lines)
            if '"""' in line:
                has_docstring = True
                output.append(line)
                for line in lines:
                    output.append(line)
                    if '"""' in line:
                        break
            else:
                has_docstring = False
            output.append("    return %s_c(%s)" % (name, args_no_types))
            output.append('')
            output.append("cdef %s_c(%s):" % (name, args))
            if not has_docstring:
                output.append(line)

        else:
            output.append(line)

    return '\n'.join(output)


def exclude_extension_in_pyver(*versions):
    def check(ext):
        return EXCLUDE_EXT if sys.version_info[:2] in versions else ext
    return check


def exclude_extension_on_platform(*platforms):
    def check(ext):
        return EXCLUDE_EXT if sys.platform in platforms else ext
    return check


def update_linetrace_extension(ext):
    ext.define_macros.append(('CYTHON_TRACE', 1))
    return ext


def update_old_numpy_extension(ext):
    update_numpy_extension(ext, set_api17_macro=False)


def update_numpy_extension(ext, set_api17_macro=True):
    import numpy
    from numpy.distutils.misc_util import get_info

    ext.include_dirs.append(numpy.get_include())

    if set_api17_macro:
        ext.define_macros.append(('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION'))

    # We need the npymath library for numpy.math.
    # This is typically a static-only library.
    for attr, value in get_info('npymath').items():
        getattr(ext, attr).extend(value)


def update_openmp_extension(ext):
    ext.openmp = True
    language = ext.language

    if sys.platform == 'win32' and sys.version_info[:2] == (3,4):
        # OpenMP tests fail in appveyor in Py3.4 -> just ignore them, EoL of Py3.4 is early 2019...
        return EXCLUDE_EXT

    if language == 'cpp':
        flags = OPENMP_CPP_COMPILER_FLAGS
    else:
        flags = OPENMP_C_COMPILER_FLAGS

    if flags:
        compile_flags, link_flags = flags
        ext.extra_compile_args.extend(compile_flags.split())
        ext.extra_link_args.extend(link_flags.split())
        return ext
    elif sys.platform == 'win32':
        return ext

    return EXCLUDE_EXT


def update_cpp11_extension(ext):
    """
        update cpp11 extensions that will run on versions of gcc >4.8
    """
    gcc_version = get_gcc_version(ext.language)
    if gcc_version:
        compiler_version = gcc_version.group(1)
        if float(compiler_version) > 4.8:
            ext.extra_compile_args.append("-std=c++11")
        return ext

    clang_version = get_clang_version(ext.language)
    if clang_version:
        ext.extra_compile_args.append("-std=c++11")
        if sys.platform == "darwin":
          ext.extra_compile_args.append("-stdlib=libc++")
          ext.extra_compile_args.append("-mmacosx-version-min=10.7")
        return ext

    return EXCLUDE_EXT


def get_cc_version(language):
    """
        finds gcc version using Popen
    """
    if language == 'cpp':
        cc = sysconfig.get_config_var('CXX')
    else:
        cc = sysconfig.get_config_var('CC')
    if not cc:
       cc = ccompiler.get_default_compiler()

    if not cc:
        return ''

    # For some reason, cc can be e.g. 'gcc -pthread'
    cc = cc.split()[0]

    # Force english output
    env = os.environ.copy()
    env['LC_MESSAGES'] = 'C'
    try:
        p = subprocess.Popen([cc, "-v"], stderr=subprocess.PIPE, env=env)
    except EnvironmentError:
        # Be compatible with Python 3
        warnings.warn("Unable to find the %s compiler: %s: %s" %
                      (language, os.strerror(sys.exc_info()[1].errno), cc))
        return ''
    _, output = p.communicate()
    return output.decode(locale.getpreferredencoding() or 'ASCII', 'replace')


def get_gcc_version(language):
    matcher = re.compile(r"gcc version (\d+\.\d+)").search
    return matcher(get_cc_version(language))


def get_clang_version(language):
    matcher = re.compile(r"clang(?:-|\s+version\s+)(\d+\.\d+)").search
    return matcher(get_cc_version(language))


def get_openmp_compiler_flags(language):
    """
    As of gcc 4.2, it supports OpenMP 2.5. Gcc 4.4 implements 3.0. We don't
    (currently) check for other compilers.

    returns a two-tuple of (CFLAGS, LDFLAGS) to build the OpenMP extension
    """
    gcc_version = get_gcc_version(language)

    if not gcc_version:
        if sys.platform == 'win32':
            return '/openmp', ''
        else:
            return None # not gcc - FIXME: do something about other compilers

    # gcc defines "__int128_t", assume that at least all 64 bit architectures have it
    global COMPILER_HAS_INT128
    COMPILER_HAS_INT128 = getattr(sys, 'maxsize', getattr(sys, 'maxint', 0)) > 2**60

    compiler_version = gcc_version.group(1)
    if compiler_version and compiler_version.split('.') >= ['4', '2']:
        return '-fopenmp', '-fopenmp'

try:
    locale.setlocale(locale.LC_ALL, '')
except locale.Error:
    pass

COMPILER = None
COMPILER_HAS_INT128 = False
OPENMP_C_COMPILER_FLAGS = get_openmp_compiler_flags('c')
OPENMP_CPP_COMPILER_FLAGS = get_openmp_compiler_flags('cpp')

# Return this from the EXT_EXTRAS matcher callback to exclude the extension
EXCLUDE_EXT = object()

EXT_EXTRAS = {
    'tag:numpy' : update_numpy_extension,
    'tag:numpy_old' : update_old_numpy_extension,
    'tag:openmp': update_openmp_extension,
    'tag:cpp11': update_cpp11_extension,
    'tag:trace' : update_linetrace_extension,
    'tag:bytesformat':  exclude_extension_in_pyver((3, 3), (3, 4)),  # no %-bytes formatting
    'tag:no-macos':  exclude_extension_on_platform('darwin'),
}


# TODO: use tags
VER_DEP_MODULES = {
    # tests are excluded if 'CurrentPythonVersion OP VersionTuple', i.e.
    # (2,4) : (operator.lt, ...) excludes ... when PyVer < 2.4.x
    (2,7) : (operator.lt, lambda x: x in ['run.withstat_py27', # multi context with statement
                                          'run.yield_inside_lambda',
                                          'run.test_dictviews',
                                          'run.pyclass_special_methods',
                                          'run.set_literals',
                                          ]),
    # The next line should start (3,); but this is a dictionary, so
    # we can only have one (3,) key.  Since 2.7 is supposed to be the
    # last 2.x release, things would have to change drastically for this
    # to be unsafe...
    (2,999): (operator.lt, lambda x: x in ['run.special_methods_T561_py3',
                                           'run.test_raisefrom',
                                           ]),
    (3,): (operator.ge, lambda x: x in ['run.non_future_division',
                                        'compile.extsetslice',
                                        'compile.extdelslice',
                                        'run.special_methods_T561_py2'
                                        ]),
    (3,3) : (operator.lt, lambda x: x in ['build.package_compilation',
                                          'run.yield_from_py33',
                                          'pyximport.pyximport_namespace',
                                          ]),
    (3,4): (operator.lt, lambda x: x in ['run.py34_signature',
                                         'run.test_unicode',  # taken from Py3.7, difficult to backport
                                         ]),
    (3,4,999): (operator.gt, lambda x: x in ['run.initial_file_path',
                                             ]),
    (3,5): (operator.lt, lambda x: x in ['run.py35_pep492_interop',
                                         'run.py35_asyncio_async_def',
                                         'run.mod__spec__',
                                         'run.pep526_variable_annotations',  # typing module
                                         'run.test_exceptions',  # copied from Py3.7+
                                         ]),
}

INCLUDE_DIRS = [ d for d in os.getenv('INCLUDE', '').split(os.pathsep) if d ]
CFLAGS = os.getenv('CFLAGS', '').split()
CCACHE = os.getenv('CYTHON_RUNTESTS_CCACHE', '').split()
TEST_SUPPORT_DIR = 'testsupport'

BACKENDS = ['c', 'cpp']

UTF8_BOM_BYTES = r'\xef\xbb\xbf'.encode('ISO-8859-1').decode('unicode_escape')


def memoize(f):
    uncomputed = object()
    f._cache = {}
    def func(*args):
        res = f._cache.get(args, uncomputed)
        if res is uncomputed:
            res = f._cache[args] = f(*args)
        return res
    return func


@memoize
def parse_tags(filepath):
    tags = defaultdict(list)
    parse_tag = re.compile(r'#\s*(\w+)\s*:(.*)$').match
    with io_open(filepath, encoding='ISO-8859-1', errors='ignore') as f:
        for line in f:
            # ignore BOM-like bytes and whitespace
            line = line.lstrip(UTF8_BOM_BYTES).strip()
            if not line:
                if tags:
                    break  # assume all tags are in one block
                else:
                    continue
            if line[0] != '#':
                break
            parsed = parse_tag(line)
            if parsed:
                tag, values = parsed.groups()
                if tag in ('coding', 'encoding'):
                    continue
                if tag == 'tags':
                    tag = 'tag'
                    print("WARNING: test tags use the 'tag' directive, not 'tags' (%s)" % filepath)
                if tag not in ('mode', 'tag', 'ticket', 'cython', 'distutils', 'preparse'):
                    print("WARNING: unknown test directive '%s' found (%s)" % (tag, filepath))
                values = values.split(',')
                tags[tag].extend(filter(None, [value.strip() for value in values]))
            elif tags:
                break  # assume all tags are in one block
    return tags


list_unchanging_dir = memoize(lambda x: os.listdir(x))


@memoize
def _list_pyregr_data_files(test_directory):
    is_data_file = re.compile('(?:[.](txt|pem|db|html)|^bad.*[.]py)$').search
    return ['__init__.py'] + [
        filename for filename in list_unchanging_dir(test_directory)
        if is_data_file(filename)]


def import_ext(module_name, file_path=None):
    if file_path:
        import imp
        return imp.load_dynamic(module_name, file_path)
    else:
        try:
            from importlib import invalidate_caches
        except ImportError:
            pass
        else:
            invalidate_caches()
        return __import__(module_name, globals(), locals(), ['*'])


class build_ext(_build_ext):
    def build_extension(self, ext):
        try:
            try: # Py2.7+ & Py3.2+
                compiler_obj = self.compiler_obj
            except AttributeError:
                compiler_obj = self.compiler
            if ext.language == 'c++':
                compiler_obj.compiler_so.remove('-Wstrict-prototypes')
            if CCACHE:
                compiler_obj.compiler_so = CCACHE + compiler_obj.compiler_so
            if getattr(ext, 'openmp', None) and compiler_obj.compiler_type == 'msvc':
                ext.extra_compile_args.append('/openmp')
        except Exception:
            pass
        _build_ext.build_extension(self, ext)


class ErrorWriter(object):
    match_error = re.compile(r'(warning:)?(?:.*:)?\s*([-0-9]+)\s*:\s*([-0-9]+)\s*:\s*(.*)').match

    def __init__(self):
        self.output = []
        self.write = self.output.append

    def _collect(self):
        s = ''.join(self.output)
        results = {'errors': [], 'warnings': []}
        for line in s.splitlines():
            match = self.match_error(line)
            if match:
                is_warning, line, column, message = match.groups()
                results['warnings' if is_warning else 'errors'].append((int(line), int(column), message.strip()))

        return [["%d:%d: %s" % values for values in sorted(results[key])] for key in ('errors', 'warnings')]

    def geterrors(self):
        return self._collect()[0]

    def getwarnings(self):
        return self._collect()[1]

    def getall(self):
        return self._collect()

    def close(self):
        pass  # ignore, only to match file-like interface


class Stats(object):
    def __init__(self, top_n=8):
        self.top_n = top_n
        self.test_counts = defaultdict(int)
        self.test_times = defaultdict(float)
        self.top_tests = defaultdict(list)

    def add_time(self, name, language, metric, t):
        self.test_counts[metric] += 1
        self.test_times[metric] += t
        top = self.top_tests[metric]
        push = heapq.heappushpop if len(top) >= self.top_n else heapq.heappush
        # min-heap => pop smallest/shortest until longest times remain
        push(top, (t, name, language))

    @contextmanager
    def time(self, name, language, metric):
        t = time.time()
        yield
        t = time.time() - t
        self.add_time(name, language, metric, t)

    def update(self, stats):
        # type: (Stats) -> None
        for metric, t in stats.test_times.items():
            self.test_times[metric] += t
            self.test_counts[metric] += stats.test_counts[metric]
            top = self.top_tests[metric]
            for entry in stats.top_tests[metric]:
                push = heapq.heappushpop if len(top) >= self.top_n else heapq.heappush
                push(top, entry)

    def print_stats(self, out=sys.stderr):
        if not self.test_times:
            return
        lines = ['Times:\n']
        for metric, t in sorted(self.test_times.items()):
            count = self.test_counts[metric]
            top = self.top_tests[metric]
            lines.append("%-12s: %8.2f sec  (%4d, %6.3f / run) - slowest: %s\n" % (
                metric, t, count, t / count,
                ', '.join("'{2}:{1}' ({0:.2f}s)".format(*item) for item in heapq.nlargest(self.top_n, top))))
        out.write(''.join(lines))


class TestBuilder(object):
    def __init__(self, rootdir, workdir, selectors, exclude_selectors, options,
                 with_pyregr, languages, test_bugs, language_level,
                 common_utility_dir, pythran_dir=None,
                 default_mode='run', stats=None,
                 add_embedded_test=False):
        self.rootdir = rootdir
        self.workdir = workdir
        self.selectors = selectors
        self.exclude_selectors = exclude_selectors
        self.annotate = options.annotate_source
        self.cleanup_workdir = options.cleanup_workdir
        self.cleanup_sharedlibs = options.cleanup_sharedlibs
        self.cleanup_failures = options.cleanup_failures
        self.with_pyregr = with_pyregr
        self.cython_only = options.cython_only
        self.languages = languages
        self.test_bugs = test_bugs
        self.fork = options.fork
        self.language_level = language_level
        self.test_determinism = options.test_determinism
        self.common_utility_dir = common_utility_dir
        self.pythran_dir = pythran_dir
        self.default_mode = default_mode
        self.stats = stats
        self.add_embedded_test = add_embedded_test

    def build_suite(self):
        suite = unittest.TestSuite()
        filenames = os.listdir(self.rootdir)
        filenames.sort()
        for filename in filenames:
            path = os.path.join(self.rootdir, filename)
            if os.path.isdir(path) and filename != TEST_SUPPORT_DIR:
                if filename == 'pyregr' and not self.with_pyregr:
                    continue
                if filename == 'broken' and not self.test_bugs:
                    continue
                suite.addTest(
                    self.handle_directory(path, filename))
        if sys.platform not in ['win32'] and self.add_embedded_test:
            # Non-Windows makefile.
            if [1 for selector in self.selectors if selector("embedded")] \
                and not [1 for selector in self.exclude_selectors if selector("embedded")]:
                suite.addTest(unittest.makeSuite(EmbedTest))
        return suite

    def handle_directory(self, path, context):
        workdir = os.path.join(self.workdir, context)
        if not os.path.exists(workdir):
            os.makedirs(workdir)

        suite = unittest.TestSuite()
        filenames = list_unchanging_dir(path)
        filenames.sort()
        for filename in filenames:
            filepath = os.path.join(path, filename)
            module, ext = os.path.splitext(filename)
            if ext not in ('.py', '.pyx', '.srctree'):
                continue
            if filename.startswith('.'):
                continue # certain emacs backup files
            if context == 'pyregr':
                tags = defaultdict(list)
            else:
                tags = parse_tags(filepath)
            fqmodule = "%s.%s" % (context, module)
            if not [ 1 for match in self.selectors
                     if match(fqmodule, tags) ]:
                continue
            if self.exclude_selectors:
                if [1 for match in self.exclude_selectors
                        if match(fqmodule, tags)]:
                    continue

            mode = self.default_mode
            if tags['mode']:
                mode = tags['mode'][0]
            elif context == 'pyregr':
                mode = 'pyregr'

            if ext == '.srctree':
                if 'cpp' not in tags['tag'] or 'cpp' in self.languages:
                    suite.addTest(EndToEndTest(filepath, workdir, self.cleanup_workdir, stats=self.stats))
                continue

            # Choose the test suite.
            if mode == 'pyregr':
                if not filename.startswith('test_'):
                    continue
                test_class = CythonPyregrTestCase
            elif mode == 'run':
                if module.startswith("test_"):
                    test_class = CythonUnitTestCase
                else:
                    test_class = CythonRunTestCase
            elif mode in ['compile', 'error']:
                test_class = CythonCompileTestCase
            else:
                raise KeyError('Invalid test mode: ' + mode)

            for test in self.build_tests(test_class, path, workdir,
                                         module, mode == 'error', tags):
                suite.addTest(test)

            if mode == 'run' and ext == '.py' and not self.cython_only and not filename.startswith('test_'):
                # additionally test file in real Python
                min_py_ver = [
                    (int(pyver.group(1)), int(pyver.group(2)))
                    for pyver in map(re.compile(r'pure([0-9]+)[.]([0-9]+)').match, tags['tag'])
                    if pyver
                ]
                if not min_py_ver or any(sys.version_info >= min_ver for min_ver in min_py_ver):
                    suite.addTest(PureDoctestTestCase(module, os.path.join(path, filename), tags, stats=self.stats))

        return suite

    def build_tests(self, test_class, path, workdir, module, expect_errors, tags):
        warning_errors = 'werror' in tags['tag']
        expect_warnings = 'warnings' in tags['tag']

        if expect_errors:
            if skip_c(tags) and 'cpp' in self.languages:
                languages = ['cpp']
            else:
                languages = self.languages[:1]
        else:
            languages = self.languages

        if skip_c(tags) and 'c' in languages:
            languages = list(languages)
            languages.remove('c')
        elif 'no-cpp' in tags['tag'] and 'cpp' in self.languages:
            languages = list(languages)
            languages.remove('cpp')

        pythran_dir = self.pythran_dir
        if 'pythran' in tags['tag'] and not pythran_dir and 'cpp' in languages:
            import pythran.config
            try:
                pythran_ext = pythran.config.make_extension(python=True)
            except TypeError:  # old pythran version syntax
                pythran_ext = pythran.config.make_extension()
            pythran_dir = pythran_ext['include_dirs'][0]

        preparse_list = tags.get('preparse', ['id'])
        tests = [ self.build_test(test_class, path, workdir, module, tags, language,
                                  expect_errors, expect_warnings, warning_errors, preparse,
                                  pythran_dir if language == "cpp" else None)
                  for language in languages
                  for preparse in preparse_list ]
        return tests

    def build_test(self, test_class, path, workdir, module, tags, language,
                   expect_errors, expect_warnings, warning_errors, preparse, pythran_dir):
        language_workdir = os.path.join(workdir, language)
        if not os.path.exists(language_workdir):
            os.makedirs(language_workdir)
        workdir = os.path.join(language_workdir, module)
        if preparse != 'id':
            workdir += '_%s' % str(preparse)
        return test_class(path, workdir, module, tags,
                          language=language,
                          preparse=preparse,
                          expect_errors=expect_errors,
                          expect_warnings=expect_warnings,
                          annotate=self.annotate,
                          cleanup_workdir=self.cleanup_workdir,
                          cleanup_sharedlibs=self.cleanup_sharedlibs,
                          cleanup_failures=self.cleanup_failures,
                          cython_only=self.cython_only,
                          fork=self.fork,
                          language_level=self.language_level,
                          warning_errors=warning_errors,
                          test_determinism=self.test_determinism,
                          common_utility_dir=self.common_utility_dir,
                          pythran_dir=pythran_dir,
                          stats=self.stats)


def skip_c(tags):
    if 'cpp' in tags['tag']:
        return True

    # We don't want to create a distutils key in the
    # dictionary so we check before looping.
    if 'distutils' in tags:
        for option in tags['distutils']:
            splitted = option.split('=')
            if len(splitted) == 2:
                argument, value = splitted
                if argument.strip() == 'language' and value.strip() == 'c++':
                    return True
    return False


def filter_stderr(stderr_bytes):
    """
    Filter annoying warnings from output.
    """
    if b"Command line warning D9025" in stderr_bytes:
        # MSCV: cl : Command line warning D9025 : overriding '/Ox' with '/Od'
        stderr_bytes = b'\n'.join(
            line for line in stderr_bytes.splitlines()
            if b"Command line warning D9025" not in line)
    return stderr_bytes


class CythonCompileTestCase(unittest.TestCase):
    def __init__(self, test_directory, workdir, module, tags, language='c', preparse='id',
                 expect_errors=False, expect_warnings=False, annotate=False, cleanup_workdir=True,
                 cleanup_sharedlibs=True, cleanup_failures=True, cython_only=False,
                 fork=True, language_level=2, warning_errors=False,
                 test_determinism=False,
                 common_utility_dir=None, pythran_dir=None, stats=None):
        self.test_directory = test_directory
        self.tags = tags
        self.workdir = workdir
        self.module = module
        self.language = language
        self.preparse = preparse
        self.name = module if self.preparse == "id" else "%s_%s" % (module, preparse)
        self.expect_errors = expect_errors
        self.expect_warnings = expect_warnings
        self.annotate = annotate
        self.cleanup_workdir = cleanup_workdir
        self.cleanup_sharedlibs = cleanup_sharedlibs
        self.cleanup_failures = cleanup_failures
        self.cython_only = cython_only
        self.fork = fork
        self.language_level = language_level
        self.warning_errors = warning_errors
        self.test_determinism = test_determinism
        self.common_utility_dir = common_utility_dir
        self.pythran_dir = pythran_dir
        self.stats = stats
        unittest.TestCase.__init__(self)

    def shortDescription(self):
        return "compiling (%s%s) %s" % (self.language, "/pythran" if self.pythran_dir is not None else "", self.name)

    def setUp(self):
        from Cython.Compiler import Options
        self._saved_options = [
            (name, getattr(Options, name))
            for name in ('warning_errors', 'clear_to_none', 'error_on_unknown_names', 'error_on_uninitialized')
        ]
        self._saved_default_directives = list(Options.get_directive_defaults().items())
        Options.warning_errors = self.warning_errors
        if sys.version_info >= (3, 4):
            Options._directive_defaults['autotestdict'] = False

        if not os.path.exists(self.workdir):
            os.makedirs(self.workdir)
        if self.workdir not in sys.path:
            sys.path.insert(0, self.workdir)

    def tearDown(self):
        from Cython.Compiler import Options
        for name, value in self._saved_options:
            setattr(Options, name, value)
        Options._directive_defaults = dict(self._saved_default_directives)
        unpatch_inspect_isfunction()

        try:
            sys.path.remove(self.workdir)
        except ValueError:
            pass
        try:
            del sys.modules[self.module]
        except KeyError:
            pass
        cleanup = self.cleanup_failures or self.success
        cleanup_c_files = WITH_CYTHON and self.cleanup_workdir and cleanup
        cleanup_lib_files = self.cleanup_sharedlibs and cleanup
        is_cygwin = sys.platform == 'cygwin'

        if os.path.exists(self.workdir):
            if cleanup_c_files and cleanup_lib_files and not is_cygwin:
                shutil.rmtree(self.workdir, ignore_errors=True)
            else:
                for rmfile in os.listdir(self.workdir):
                    if not cleanup_c_files:
                        if (rmfile[-2:] in (".c", ".h") or
                                rmfile[-4:] == ".cpp" or
                                rmfile.endswith(".html") and rmfile.startswith(self.module)):
                            continue

                    is_shared_obj = rmfile.endswith(".so") or rmfile.endswith(".dll")

                    if not cleanup_lib_files and is_shared_obj:
                        continue

                    try:
                        rmfile = os.path.join(self.workdir, rmfile)
                        if os.path.isdir(rmfile):
                            shutil.rmtree(rmfile, ignore_errors=True)
                        elif is_cygwin and is_shared_obj:
                            # Delete later
                            _to_clean.append(rmfile)
                        else:
                            os.remove(rmfile)
                    except IOError:
                        pass

                if cleanup_c_files and cleanup_lib_files and is_cygwin:
                    # Finally, remove the work dir itself
                    _to_clean.append(self.workdir)

        if cleanup_c_files and os.path.exists(self.workdir + '-again'):
            shutil.rmtree(self.workdir + '-again', ignore_errors=True)


    def runTest(self):
        self.success = False
        self.runCompileTest()
        self.success = True

    def runCompileTest(self):
        return self.compile(
            self.test_directory, self.module, self.workdir,
            self.test_directory, self.expect_errors, self.expect_warnings, self.annotate)

    def find_module_source_file(self, source_file):
        if not os.path.exists(source_file):
            source_file = source_file[:-1]
        return source_file

    def build_target_filename(self, module_name):
        target = '%s.%s' % (module_name, self.language)
        return target

    def related_files(self, test_directory, module_name):
        is_related = re.compile('%s_.*[.].*' % module_name).match
        return [filename for filename in list_unchanging_dir(test_directory)
                if is_related(filename)]

    def copy_files(self, test_directory, target_directory, file_list):
        if self.preparse and self.preparse != 'id':
            preparse_func = globals()[self.preparse]
            def copy(src, dest):
                with open(src) as fin:
                    with open(dest, 'w') as fout:
                        fout.write(preparse_func(fin.read()))
        else:
            # use symlink on Unix, copy on Windows
            try:
                copy = os.symlink
            except AttributeError:
                copy = shutil.copy

        join = os.path.join
        for filename in file_list:
            file_path = join(test_directory, filename)
            if os.path.exists(file_path):
                copy(file_path, join(target_directory, filename))

    def source_files(self, workdir, module_name, file_list):
        return ([self.build_target_filename(module_name)] +
            [filename for filename in file_list
             if not os.path.isfile(os.path.join(workdir, filename))])

    def split_source_and_output(self, test_directory, module, workdir):
        source_file = self.find_module_source_file(os.path.join(test_directory, module) + '.pyx')
        with io_open(source_file, 'r', encoding='ISO-8859-1') as source_and_output:
            error_writer = warnings_writer = None
            out = io_open(os.path.join(workdir, module + os.path.splitext(source_file)[1]),
                          'w', encoding='ISO-8859-1')
            try:
                for line in source_and_output:
                    if line.startswith("_ERRORS"):
                        out.close()
                        out = error_writer = ErrorWriter()
                    elif line.startswith("_WARNINGS"):
                        out.close()
                        out = warnings_writer = ErrorWriter()
                    else:
                        out.write(line)
            finally:
                out.close()

        return (error_writer.geterrors() if error_writer else [],
                warnings_writer.geterrors() if warnings_writer else [])

    def run_cython(self, test_directory, module, targetdir, incdir, annotate,
                   extra_compile_options=None):
        include_dirs = INCLUDE_DIRS + [os.path.join(test_directory, '..', TEST_SUPPORT_DIR)]
        if incdir:
            include_dirs.append(incdir)

        if self.preparse == 'id':
            source = self.find_module_source_file(
                os.path.join(test_directory, module + '.pyx'))
        else:
            self.copy_files(test_directory, targetdir, [module + '.pyx'])
            source = os.path.join(targetdir, module + '.pyx')
        target = os.path.join(targetdir, self.build_target_filename(module))

        if extra_compile_options is None:
            extra_compile_options = {}

        if 'allow_unknown_names' in self.tags['tag']:
            from Cython.Compiler import Options
            Options.error_on_unknown_names = False

        try:
            CompilationOptions
        except NameError:
            from Cython.Compiler.Main import CompilationOptions
            from Cython.Compiler.Main import compile as cython_compile
            from Cython.Compiler.Main import default_options
        common_utility_include_dir = self.common_utility_dir

        options = CompilationOptions(
            default_options,
            include_path = include_dirs,
            output_file = target,
            annotate = annotate,
            use_listing_file = False,
            cplus = self.language == 'cpp',
            np_pythran = self.pythran_dir is not None,
            language_level = self.language_level,
            generate_pxi = False,
            evaluate_tree_assertions = True,
            common_utility_include_dir = common_utility_include_dir,
            **extra_compile_options
            )
        cython_compile(source, options=options,
                       full_module_name=module)

    def run_distutils(self, test_directory, module, workdir, incdir,
                      extra_extension_args=None):
        cwd = os.getcwd()
        os.chdir(workdir)
        try:
            build_extension = build_ext(get_distutils_distro())
            build_extension.include_dirs = INCLUDE_DIRS[:]
            if incdir:
                build_extension.include_dirs.append(incdir)
            build_extension.finalize_options()
            if COMPILER:
                build_extension.compiler = COMPILER

            ext_compile_flags = CFLAGS[:]

            if  build_extension.compiler == 'mingw32':
                ext_compile_flags.append('-Wno-format')
            if extra_extension_args is None:
                extra_extension_args = {}

            related_files = self.related_files(test_directory, module)
            self.copy_files(test_directory, workdir, related_files)

            from distutils.core import Extension
            extension = Extension(
                module,
                sources=self.source_files(workdir, module, related_files),
                extra_compile_args=ext_compile_flags,
                **extra_extension_args
                )

            if self.language == 'cpp':
                # Set the language now as the fixer might need it
                extension.language = 'c++'

            if 'distutils' in self.tags:
                from Cython.Build.Dependencies import DistutilsInfo
                from Cython.Utils import open_source_file
                pyx_path = os.path.join(self.test_directory, self.module + ".pyx")
                with open_source_file(pyx_path) as f:
                    DistutilsInfo(f).apply(extension)

            if self.pythran_dir:
                from Cython.Build.Dependencies import update_pythran_extension
                update_pythran_extension(extension)

            for matcher, fixer in list(EXT_EXTRAS.items()):
                if isinstance(matcher, str):
                    # lazy init
                    del EXT_EXTRAS[matcher]
                    matcher = string_selector(matcher)
                    EXT_EXTRAS[matcher] = fixer
                if matcher(module, self.tags):
                    newext = fixer(extension)
                    if newext is EXCLUDE_EXT:
                        return skip_test("Test '%s' excluded due to tags '%s'" % (
                            self.name, ', '.join(self.tags.get('tag', ''))))
                    extension = newext or extension
            if self.language == 'cpp':
                extension.language = 'c++'
            build_extension.extensions = [extension]
            build_extension.build_temp = workdir
            build_extension.build_lib  = workdir
            build_extension.run()
        finally:
            os.chdir(cwd)

        try:
            get_ext_fullpath = build_extension.get_ext_fullpath
        except AttributeError:
            def get_ext_fullpath(ext_name, self=build_extension):
                # copied from distutils.command.build_ext (missing in Py2.[45])
                fullname = self.get_ext_fullname(ext_name)
                modpath = fullname.split('.')
                filename = self.get_ext_filename(modpath[-1])
                if not self.inplace:
                    filename = os.path.join(*modpath[:-1]+[filename])
                    return os.path.join(self.build_lib, filename)
                package = '.'.join(modpath[0:-1])
                build_py = self.get_finalized_command('build_py')
                package_dir = os.path.abspath(build_py.get_package_dir(package))
                return os.path.join(package_dir, filename)

        return get_ext_fullpath(module)

    def compile(self, test_directory, module, workdir, incdir,
                expect_errors, expect_warnings, annotate):
        expected_errors = expected_warnings = errors = warnings = ()
        if expect_errors or expect_warnings:
            expected_errors, expected_warnings = self.split_source_and_output(
                test_directory, module, workdir)
            test_directory = workdir

        if WITH_CYTHON:
            old_stderr = sys.stderr
            try:
                sys.stderr = ErrorWriter()
                with self.stats.time(self.name, self.language, 'cython'):
                    self.run_cython(test_directory, module, workdir, incdir, annotate)
                errors, warnings = sys.stderr.getall()
            finally:
                sys.stderr = old_stderr
            if self.test_determinism and not expect_errors:
                workdir2 = workdir + '-again'
                os.mkdir(workdir2)
                self.run_cython(test_directory, module, workdir2, incdir, annotate)
                diffs = []
                for file in os.listdir(workdir2):
                    if (open(os.path.join(workdir, file)).read()
                        != open(os.path.join(workdir2, file)).read()):
                        diffs.append(file)
                        os.system('diff -u %s/%s %s/%s > %s/%s.diff' % (
                            workdir, file,
                            workdir2, file,
                            workdir2, file))
                if diffs:
                    self.fail('Nondeterministic file generation: %s' % ', '.join(diffs))

        tostderr = sys.__stderr__.write
        if expected_warnings or (expect_warnings and warnings):
            self._match_output(expected_warnings, warnings, tostderr)
        if 'cerror' in self.tags['tag']:
            if errors:
                tostderr("\n=== Expected C compile error ===\n")
                tostderr("\n=== Got Cython errors: ===\n")
                tostderr('\n'.join(errors))
                tostderr('\n\n')
                raise RuntimeError('should have generated extension code')
        elif errors or expected_errors:
            self._match_output(expected_errors, errors, tostderr)
            return None

        so_path = None
        if not self.cython_only:
            from Cython.Utils import captured_fd, print_bytes
            from distutils.errors import CompileError, LinkError
            show_output = True
            get_stderr = get_stdout = None
            try:
                with captured_fd(1) as get_stdout:
                    with captured_fd(2) as get_stderr:
                        with self.stats.time(self.name, self.language, 'compile-%s' % self.language):
                            so_path = self.run_distutils(test_directory, module, workdir, incdir)
            except Exception as exc:
                if ('cerror' in self.tags['tag'] and
                    ((get_stderr and get_stderr()) or
                     isinstance(exc, (CompileError, LinkError)))):
                    show_output = False  # expected C compiler failure
                else:
                    raise
            else:
                if 'cerror' in self.tags['tag']:
                    raise RuntimeError('should have failed C compile')
            finally:
                if show_output:
                    stdout = get_stdout and get_stdout().strip()
                    if stdout:
                        print_bytes(
                            stdout, header_text="\n=== C/C++ compiler output: =========\n",
                            end=None, file=sys.__stderr__)
                    stderr = get_stderr and filter_stderr(get_stderr()).strip()
                    if stderr:
                        print_bytes(
                            stderr, header_text="\n=== C/C++ compiler error output: ===\n",
                            end=None, file=sys.__stderr__)
                    if stdout or stderr:
                        tostderr("\n====================================\n")
        return so_path

    def _match_output(self, expected_output, actual_output, write):
        try:
            for expected, actual in zip(expected_output, actual_output):
                self.assertEqual(expected, actual)
            if len(actual_output) < len(expected_output):
                expected = expected_output[len(actual_output)]
                self.assertEqual(expected, None)
            elif len(actual_output) > len(expected_output):
                unexpected = actual_output[len(expected_output)]
                self.assertEqual(None, unexpected)
        except AssertionError:
            write("\n=== Expected: ===\n")
            write('\n'.join(expected_output))
            write("\n\n=== Got: ===\n")
            write('\n'.join(actual_output))
            write('\n\n')
            raise


class CythonRunTestCase(CythonCompileTestCase):
    def setUp(self):
        CythonCompileTestCase.setUp(self)
        from Cython.Compiler import Options
        Options.clear_to_none = False

    def shortDescription(self):
        if self.cython_only:
            return CythonCompileTestCase.shortDescription(self)
        else:
            return "compiling (%s%s) and running %s" % (self.language, "/pythran" if self.pythran_dir is not None else "", self.name)

    def run(self, result=None):
        if result is None:
            result = self.defaultTestResult()
        result.startTest(self)
        try:
            self.setUp()
            try:
                self.success = False
                ext_so_path = self.runCompileTest()
                # Py2.6 lacks "_TextTestResult.skipped"
                failures, errors, skipped = len(result.failures), len(result.errors), len(getattr(result, 'skipped', []))
                if not self.cython_only and ext_so_path is not None:
                    self.run_tests(result, ext_so_path)
                if failures == len(result.failures) and errors == len(result.errors):
                    # No new errors...
                    self.success = True
            finally:
                check_thread_termination()
        except SkipTest as exc:
            result.addSkip(self, str(exc))
            result.stopTest(self)
        except Exception:
            result.addError(self, sys.exc_info())
            result.stopTest(self)
        try:
            self.tearDown()
        except Exception:
            pass

    def run_tests(self, result, ext_so_path):
        self.run_doctests(self.module, result, ext_so_path)

    def run_doctests(self, module_or_name, result, ext_so_path):
        def run_test(result):
            if isinstance(module_or_name, basestring):
                with self.stats.time(self.name, self.language, 'import'):
                    module = import_ext(module_or_name, ext_so_path)
            else:
                module = module_or_name
            tests = doctest.DocTestSuite(module)
            with self.stats.time(self.name, self.language, 'run'):
                tests.run(result)
        run_forked_test(result, run_test, self.shortDescription(), self.fork)


def run_forked_test(result, run_func, test_name, fork=True):
    if not fork or sys.version_info[0] >= 3 or not hasattr(os, 'fork'):
        run_func(result)
        sys.stdout.flush()
        sys.stderr.flush()
        gc.collect()
        return

    # fork to make sure we do not keep the tested module loaded
    result_handle, result_file = tempfile.mkstemp()
    os.close(result_handle)
    child_id = os.fork()
    if not child_id:
        result_code = 0
        try:
            try:
                tests = partial_result = None
                try:
                    partial_result = PartialTestResult(result)
                    run_func(partial_result)
                    sys.stdout.flush()
                    sys.stderr.flush()
                    gc.collect()
                except Exception:
                    result_code = 1
                    if partial_result is not None:
                        if tests is None:
                            # importing failed, try to fake a test class
                            tests = _FakeClass(
                                failureException=sys.exc_info()[1],
                                _shortDescription=test_name,
                                module_name=None)
                        partial_result.addError(tests, sys.exc_info())
                if partial_result is not None:
                    with open(result_file, 'wb') as output:
                        pickle.dump(partial_result.data(), output)
            except:
                traceback.print_exc()
        finally:
            try: sys.stderr.flush()
            except: pass
            try: sys.stdout.flush()
            except: pass
            os._exit(result_code)

    try:
        cid, result_code = os.waitpid(child_id, 0)
        module_name = test_name.split()[-1]
        # os.waitpid returns the child's result code in the
        # upper byte of result_code, and the signal it was
        # killed by in the lower byte
        if result_code & 255:
            raise Exception(
                "Tests in module '%s' were unexpectedly killed by signal %d, see test output for details." % (
                    module_name, result_code & 255))
        result_code >>= 8
        if result_code in (0,1):
            try:
                with open(result_file, 'rb') as f:
                    PartialTestResult.join_results(result, pickle.load(f))
            except Exception:
                raise Exception(
                    "Failed to load test result from test in module '%s' after exit status %d,"
                    " see test output for details." % (module_name, result_code))
        if result_code:
            raise Exception(
                "Tests in module '%s' exited with status %d, see test output for details." % (
                    module_name, result_code))
    finally:
        try:
            os.unlink(result_file)
        except:
            pass


class PureDoctestTestCase(unittest.TestCase):
    def __init__(self, module_name, module_path, tags, stats=None):
        self.tags = tags
        self.module_name = self.name = module_name
        self.module_path = module_path
        self.stats = stats
        unittest.TestCase.__init__(self, 'run')

    def shortDescription(self):
        return "running pure doctests in %s" % self.module_name

    def run(self, result=None):
        if result is None:
            result = self.defaultTestResult()
        loaded_module_name = 'pure_doctest__' + self.module_name
        result.startTest(self)
        try:
            self.setUp()

            import imp
            with self.stats.time(self.name, 'py', 'pyimport'):
                m = imp.load_source(loaded_module_name, self.module_path)
            try:
                with self.stats.time(self.name, 'py', 'pyrun'):
                    doctest.DocTestSuite(m).run(result)
            finally:
                del m
                if loaded_module_name in sys.modules:
                    del sys.modules[loaded_module_name]
                check_thread_termination()
        except Exception:
            result.addError(self, sys.exc_info())
            result.stopTest(self)
        try:
            self.tearDown()
        except Exception:
            pass

        if 'mypy' in self.tags['tag']:
            try:
                from mypy import api as mypy_api
            except ImportError:
                pass
            else:
                with self.stats.time(self.name, 'py', 'mypy'):
                    mypy_result = mypy_api.run([
                        self.module_path,
                        '--ignore-missing-imports',
                        '--follow-imports', 'skip',
                    ])
                if mypy_result[2]:
                    self.fail(mypy_result[0])


is_private_field = re.compile('^_[^_]').match

class _FakeClass(object):
    def __init__(self, **kwargs):
        self._shortDescription = kwargs.get('module_name')
        self.__dict__.update(kwargs)
    def shortDescription(self):
        return self._shortDescription

try: # Py2.7+ and Py3.2+
    from unittest.runner import _TextTestResult
except ImportError:
    from unittest import _TextTestResult

class PartialTestResult(_TextTestResult):
    def __init__(self, base_result):
        _TextTestResult.__init__(
            self, self._StringIO(), True,
            base_result.dots + base_result.showAll*2)
        try:
            self.skipped
        except AttributeError:
            self.skipped = []  # Py2.6

    def strip_error_results(self, results):
        for test_case, error in results:
            for attr_name in filter(is_private_field, dir(test_case)):
                if attr_name == '_dt_test':
                    test_case._dt_test = _FakeClass(
                        name=test_case._dt_test.name)
                elif attr_name != '_shortDescription':
                    setattr(test_case, attr_name, None)

    def data(self):
        self.strip_error_results(self.failures)
        self.strip_error_results(self.errors)
        return (self.failures, self.errors, self.skipped, self.testsRun,
                self.stream.getvalue())

    def join_results(result, data):
        """Static method for merging the result back into the main
        result object.
        """
        failures, errors, skipped, tests_run, output = data
        if output:
            result.stream.write(output)
        result.errors.extend(errors)
        try:
            result.skipped.extend(skipped)
        except AttributeError:
            pass  # Py2.6
        result.failures.extend(failures)
        result.testsRun += tests_run

    join_results = staticmethod(join_results)

    class _StringIO(StringIO):
        def writeln(self, line):
            self.write("%s\n" % line)


class CythonUnitTestCase(CythonRunTestCase):
    def shortDescription(self):
        return "compiling (%s) tests in %s" % (self.language, self.name)

    def run_tests(self, result, ext_so_path):
        with self.stats.time(self.name, self.language, 'import'):
            module = import_ext(self.module, ext_so_path)
        tests = unittest.defaultTestLoader.loadTestsFromModule(module)
        with self.stats.time(self.name, self.language, 'run'):
            tests.run(result)


class CythonPyregrTestCase(CythonRunTestCase):
    def setUp(self):
        CythonRunTestCase.setUp(self)
        from Cython.Compiler import Options
        Options.error_on_unknown_names = False
        Options.error_on_uninitialized = False
        Options._directive_defaults.update(dict(
            binding=True, always_allow_keywords=True,
            set_initial_path="SOURCEFILE"))
        patch_inspect_isfunction()

    def related_files(self, test_directory, module_name):
        return _list_pyregr_data_files(test_directory)

    def _run_unittest(self, result, *classes):
        """Run tests from unittest.TestCase-derived classes."""
        valid_types = (unittest.TestSuite, unittest.TestCase)
        suite = unittest.TestSuite()
        for cls in classes:
            if isinstance(cls, str):
                if cls in sys.modules:
                    suite.addTest(unittest.findTestCases(sys.modules[cls]))
                else:
                    raise ValueError("str arguments must be keys in sys.modules")
            elif isinstance(cls, valid_types):
                suite.addTest(cls)
            else:
                suite.addTest(unittest.makeSuite(cls))
        with self.stats.time(self.name, self.language, 'run'):
            suite.run(result)

    def _run_doctest(self, result, module):
        self.run_doctests(module, result, None)

    def run_tests(self, result, ext_so_path):
        try:
            from test import support
        except ImportError: # Python2.x
            from test import test_support as support

        def run_test(result):
            def run_unittest(*classes):
                return self._run_unittest(result, *classes)
            def run_doctest(module, verbosity=None):
                return self._run_doctest(result, module)

            backup = (support.run_unittest, support.run_doctest)
            support.run_unittest = run_unittest
            support.run_doctest = run_doctest

            try:
                try:
                    sys.stdout.flush() # helps in case of crashes
                    with self.stats.time(self.name, self.language, 'import'):
                        module = import_ext(self.module, ext_so_path)
                    sys.stdout.flush() # helps in case of crashes
                    if hasattr(module, 'test_main'):
                        # help 'doctest.DocFileTest' find the module path through frame inspection
                        fake_caller_module_globals = {
                            'module': module,
                            '__name__': module.__name__,
                        }
                        call_tests = eval(
                            'lambda: module.test_main()',
                            fake_caller_module_globals, fake_caller_module_globals)
                        call_tests()
                        sys.stdout.flush() # helps in case of crashes
                except (unittest.SkipTest, support.ResourceDenied):
                    result.addSkip(self, 'ok')
            finally:
                support.run_unittest, support.run_doctest = backup

        run_forked_test(result, run_test, self.shortDescription(), self.fork)


class TestCodeFormat(unittest.TestCase):

    def __init__(self, cython_dir):
        self.cython_dir = cython_dir
        unittest.TestCase.__init__(self)

    def runTest(self):
        import pycodestyle
        config_file = os.path.join(self.cython_dir, "tox.ini")
        if not os.path.exists(config_file):
            config_file=os.path.join(os.path.dirname(__file__), "tox.ini")
        paths = glob.glob(os.path.join(self.cython_dir, "**/*.py"), recursive=True)
        style = pycodestyle.StyleGuide(config_file=config_file)
        print("")  # Fix the first line of the report.
        result = style.check_files(paths)
        self.assertEqual(result.total_errors, 0, "Found code style errors.")


include_debugger = IS_CPYTHON


def collect_unittests(path, module_prefix, suite, selectors, exclude_selectors):
    def file_matches(filename):
        return filename.startswith("Test") and filename.endswith(".py")

    def package_matches(dirname):
        return dirname == "Tests"

    loader = unittest.TestLoader()

    if include_debugger:
        skipped_dirs = []
    else:
        skipped_dirs = ['Cython' + os.path.sep + 'Debugger' + os.path.sep]

    for dirpath, dirnames, filenames in os.walk(path):
        if dirpath != path and "__init__.py" not in filenames:
            skipped_dirs.append(dirpath + os.path.sep)
            continue
        skip = False
        for dir in skipped_dirs:
            if dirpath.startswith(dir):
                skip = True
        if skip:
            continue
        parentname = os.path.split(dirpath)[-1]
        if package_matches(parentname):
            for f in filenames:
                if file_matches(f):
                    filepath = os.path.join(dirpath, f)[:-len(".py")]
                    modulename = module_prefix + filepath[len(path)+1:].replace(os.path.sep, '.')
                    if not any(1 for match in selectors if match(modulename)):
                        continue
                    if any(1 for match in exclude_selectors if match(modulename)):
                        continue
                    module = __import__(modulename)
                    for x in modulename.split('.')[1:]:
                        module = getattr(module, x)
                    suite.addTests([loader.loadTestsFromModule(module)])


def collect_doctests(path, module_prefix, suite, selectors, exclude_selectors):
    def package_matches(dirname):
        if dirname == 'Debugger' and not include_debugger:
            return False
        return dirname not in ("Mac", "Distutils", "Plex", "Tempita")
    def file_matches(filename):
        filename, ext = os.path.splitext(filename)
        blacklist = ['libcython', 'libpython', 'test_libcython_in_gdb',
                     'TestLibCython']
        return (ext == '.py' and not
                '~' in filename and not
                '#' in filename and not
                filename.startswith('.') and not
                filename in blacklist)
    import doctest
    for dirpath, dirnames, filenames in os.walk(path):
        for dir in list(dirnames):
            if not package_matches(dir):
                dirnames.remove(dir)
        for f in filenames:
            if file_matches(f):
                if not f.endswith('.py'): continue
                filepath = os.path.join(dirpath, f)
                if os.path.getsize(filepath) == 0: continue
                filepath = filepath[:-len(".py")]
                modulename = module_prefix + filepath[len(path)+1:].replace(os.path.sep, '.')
                if not [ 1 for match in selectors if match(modulename) ]:
                    continue
                if [ 1 for match in exclude_selectors if match(modulename) ]:
                    continue
                if 'in_gdb' in modulename:
                    # These should only be imported from gdb.
                    continue
                module = __import__(modulename)
                for x in modulename.split('.')[1:]:
                    module = getattr(module, x)
                if hasattr(module, "__doc__") or hasattr(module, "__test__"):
                    try:
                        suite.addTest(doctest.DocTestSuite(module))
                    except ValueError: # no tests
                        pass


class EndToEndTest(unittest.TestCase):
    """
    This is a test of build/*.srctree files, where srctree defines a full
    directory structure and its header gives a list of commands to run.
    """
    cython_root = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, treefile, workdir, cleanup_workdir=True, stats=None):
        self.name = os.path.splitext(os.path.basename(treefile))[0]
        self.treefile = treefile
        self.workdir = os.path.join(workdir, self.name)
        self.cleanup_workdir = cleanup_workdir
        self.stats = stats
        cython_syspath = [self.cython_root]
        for path in sys.path:
            if path.startswith(self.cython_root) and path not in cython_syspath:
                # Py3 installation and refnanny build prepend their
                # fixed paths to sys.path => prefer that over the
                # generic one (cython_root itself goes last)
                cython_syspath.append(path)
        self.cython_syspath = os.pathsep.join(cython_syspath[::-1])
        unittest.TestCase.__init__(self)

    def shortDescription(self):
        return "End-to-end %s" % self.name

    def setUp(self):
        from Cython.TestUtils import unpack_source_tree
        _, self.commands = unpack_source_tree(self.treefile, self.workdir)
        self.old_dir = os.getcwd()
        os.chdir(self.workdir)
        if self.workdir not in sys.path:
            sys.path.insert(0, self.workdir)

    def tearDown(self):
        if self.cleanup_workdir:
            for trial in range(5):
                try:
                    shutil.rmtree(self.workdir)
                except OSError:
                    time.sleep(0.1)
                else:
                    break
        os.chdir(self.old_dir)

    def _try_decode(self, content):
        try:
            return content.decode()
        except UnicodeDecodeError:
            return content.decode('iso-8859-1')

    def runTest(self):
        self.success = False
        commands = (self.commands
            .replace("CYTHON", "PYTHON %s" % os.path.join(self.cython_root, 'cython.py'))
            .replace("PYTHON", sys.executable))
        old_path = os.environ.get('PYTHONPATH')
        env = dict(os.environ)
        new_path = self.cython_syspath
        if old_path:
            new_path = new_path + os.pathsep + old_path
        env['PYTHONPATH'] = new_path
        cmd = []
        out = []
        err = []
        for command_no, command in enumerate(filter(None, commands.splitlines()), 1):
            with self.stats.time('%s(%d)' % (self.name, command_no), 'c',
                                 'etoe-build' if ' setup.py ' in command else 'etoe-run'):
                p = subprocess.Popen(command,
                                     stderr=subprocess.PIPE,
                                     stdout=subprocess.PIPE,
                                     shell=True,
                                     env=env)
                _out, _err = p.communicate()
                cmd.append(command)
                out.append(_out)
                err.append(_err)
            res = p.returncode
            if res != 0:
                for c, o, e in zip(cmd, out, err):
                    sys.stderr.write("%s\n%s\n%s\n\n" % (
                        c, self._try_decode(o), self._try_decode(e)))
            self.assertEqual(0, res, "non-zero exit status")
        self.success = True


# TODO: Support cython_freeze needed here as well.
# TODO: Windows support.

class EmbedTest(unittest.TestCase):

    working_dir = "Demos/embed"

    def setUp(self):
        self.old_dir = os.getcwd()
        os.chdir(self.working_dir)
        os.system(
            "make PYTHON='%s' clean > /dev/null" % sys.executable)

    def tearDown(self):
        try:
            os.system(
                "make PYTHON='%s' clean > /dev/null" % sys.executable)
        except:
            pass
        os.chdir(self.old_dir)

    def test_embed(self):
        libname = sysconfig.get_config_var('LIBRARY')
        libdir = sysconfig.get_config_var('LIBDIR')
        if not os.path.isdir(libdir) or libname not in os.listdir(libdir):
            libdir = os.path.join(os.path.dirname(sys.executable), '..', 'lib')
            if not os.path.isdir(libdir) or libname not in os.listdir(libdir):
                libdir = os.path.join(libdir, 'python%d.%d' % sys.version_info[:2], 'config')
                if not os.path.isdir(libdir) or libname not in os.listdir(libdir):
                    # report the error for the original directory
                    libdir = sysconfig.get_config_var('LIBDIR')
        cython = 'cython.py'
        if sys.version_info[0] >=3 and CY3_DIR:
            cython = os.path.join(CY3_DIR, cython)
        cython = os.path.abspath(os.path.join('..', '..', cython))
        self.assertEqual(0, os.system(
            "make PYTHON='%s' CYTHON='%s' LIBDIR1='%s' test > make.output" % (sys.executable, cython, libdir)))
        try:
            os.remove('make.output')
        except OSError:
            pass


class MissingDependencyExcluder(object):
    def __init__(self, deps):
        # deps: { matcher func : module name }
        self.exclude_matchers = []
        for matcher, mod in deps.items():
            try:
                __import__(mod)
            except ImportError:
                self.exclude_matchers.append(string_selector(matcher))
        self.tests_missing_deps = []
    def __call__(self, testname, tags=None):
        for matcher in self.exclude_matchers:
            if matcher(testname, tags):
                self.tests_missing_deps.append(testname)
                return True
        return False


class VersionDependencyExcluder(object):
    def __init__(self, deps):
        # deps: { version : matcher func }
        from sys import version_info
        self.exclude_matchers = []
        for ver, (compare, matcher) in deps.items():
            if compare(version_info, ver):
                self.exclude_matchers.append(matcher)
        self.tests_missing_deps = []
    def __call__(self, testname, tags=None):
        for matcher in self.exclude_matchers:
            if matcher(testname):
                self.tests_missing_deps.append(testname)
                return True
        return False


class FileListExcluder(object):
    def __init__(self, list_file, verbose=False):
        self.verbose = verbose
        self.excludes = {}
        self._list_file = os.path.relpath(list_file)
        with open(list_file) as f:
            for line in f:
                line = line.strip()
                if line and line[0] != '#':
                    self.excludes[line.split()[0]] = True

    def __call__(self, testname, tags=None):
        exclude = (testname in self.excludes
                   or testname.split('.')[-1] in self.excludes)
        if exclude and self.verbose:
            print("Excluding %s because it's listed in %s"
                  % (testname, self._list_file))
        return exclude


class TagsSelector(object):
    def __init__(self, tag, value):
        self.tag = tag
        self.value = value

    def __call__(self, testname, tags=None):
        if tags is None:
            return False
        else:
            return self.value in tags[self.tag]


class RegExSelector(object):
    def __init__(self, pattern_string):
        try:
            self.regex_matches = re.compile(pattern_string, re.I|re.U).search
        except re.error:
            print('Invalid pattern: %r' % pattern_string)
            raise

    def __call__(self, testname, tags=None):
        return self.regex_matches(testname)


def string_selector(s):
    if ':' in s:
        return TagsSelector(*s.split(':', 1))
    else:
        return RegExSelector(s)


class ShardExcludeSelector(object):
    # This is an exclude selector so it can override the (include) selectors.
    # It may not provide uniform distribution (in time or count), but is a
    # determanistic partition of the tests which is important.
    def __init__(self, shard_num, shard_count):
        self.shard_num = shard_num
        self.shard_count = shard_count

    def __call__(self, testname, tags=None, _hash=zlib.crc32, _is_py2=sys.version_info[0] < 3):
        # Cannot use simple hash() here as shard processes might use different hash seeds.
        # CRC32 is fast and simple, but might return negative values in Py2.
        hashval = _hash(testname) & 0x7fffffff if _is_py2 else _hash(testname.encode())
        return hashval % self.shard_count != self.shard_num


class PendingThreadsError(RuntimeError):
    pass

threads_seen = []

def check_thread_termination(ignore_seen=True):
    if threading is None: # no threading enabled in CPython
        return
    current = threading.currentThread()
    blocking_threads = []
    for t in threading.enumerate():
        if not t.isAlive() or t == current or t.name == 'time_stamper':
            continue
        t.join(timeout=2)
        if t.isAlive():
            if not ignore_seen:
                blocking_threads.append(t)
                continue
            for seen in threads_seen:
                if t is seen:
                    break
            else:
                threads_seen.append(t)
                blocking_threads.append(t)
    if not blocking_threads:
        return
    sys.stderr.write("warning: left-over threads found after running test:\n")
    for t in blocking_threads:
        sys.stderr.write('...%s\n'  % repr(t))
    raise PendingThreadsError("left-over threads found after running test")

def subprocess_output(cmd):
    try:
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return p.communicate()[0].decode('UTF-8')
    except OSError:
        return ''

def get_version():
    from Cython.Compiler.Version import version as cython_version
    full_version = cython_version
    top = os.path.dirname(os.path.abspath(__file__))
    if os.path.exists(os.path.join(top, '.git')):
        old_dir = os.getcwd()
        try:
            os.chdir(top)
            head_commit = subprocess_output(['git', 'rev-parse', 'HEAD']).strip()
            version_commit = subprocess_output(['git', 'rev-parse', cython_version]).strip()
            diff = subprocess_output(['git', 'diff', '--stat']).strip()
            if head_commit != version_commit:
                full_version += " " + head_commit
            if diff:
                full_version += ' + uncommitted changes'
        finally:
            os.chdir(old_dir)
    return full_version

_orig_stdout, _orig_stderr = sys.stdout, sys.stderr
def flush_and_terminate(status):
    try:
        _orig_stdout.flush()
        _orig_stderr.flush()
    finally:
        os._exit(status)

def main():

    global DISTDIR, WITH_CYTHON
    DISTDIR = os.path.join(os.getcwd(), os.path.dirname(sys.argv[0]))

    from Cython.Compiler import DebugFlags
    args = []
    for arg in sys.argv[1:]:
        if arg.startswith('--debug') and arg[2:].replace('-', '_') in dir(DebugFlags):
            setattr(DebugFlags, arg[2:].replace('-', '_'), True)
        else:
            args.append(arg)

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--no-cleanup", dest="cleanup_workdir",
                      action="store_false", default=True,
                      help="do not delete the generated C files (allows passing --no-cython on next run)")
    parser.add_option("--no-cleanup-sharedlibs", dest="cleanup_sharedlibs",
                      action="store_false", default=True,
                      help="do not delete the generated shared library files (allows manual module experimentation)")
    parser.add_option("--no-cleanup-failures", dest="cleanup_failures",
                      action="store_false", default=True,
                      help="enable --no-cleanup and --no-cleanup-sharedlibs for failed tests only")
    parser.add_option("--no-cython", dest="with_cython",
                      action="store_false", default=True,
                      help="do not run the Cython compiler, only the C compiler")
    parser.add_option("--compiler", dest="compiler", default=None,
                      help="C compiler type")
    backend_list = ','.join(BACKENDS)
    parser.add_option("--backends", dest="backends", default=backend_list,
                      help="select backends to test (default: %s)" % backend_list)
    parser.add_option("--no-c", dest="use_c",
                      action="store_false", default=True,
                      help="do not test C compilation backend")
    parser.add_option("--no-cpp", dest="use_cpp",
                      action="store_false", default=True,
                      help="do not test C++ compilation backend")
    parser.add_option("--no-unit", dest="unittests",
                      action="store_false", default=True,
                      help="do not run the unit tests")
    parser.add_option("--no-doctest", dest="doctests",
                      action="store_false", default=True,
                      help="do not run the doctests")
    parser.add_option("--no-file", dest="filetests",
                      action="store_false", default=True,
                      help="do not run the file based tests")
    parser.add_option("--no-pyregr", dest="pyregr",
                      action="store_false", default=True,
                      help="do not run the regression tests of CPython in tests/pyregr/")
    parser.add_option("--no-examples", dest="examples",
                      action="store_false", default=True,
                      help="Do not run the documentation tests in the examples directory.")
    parser.add_option("--no-code-style", dest="code_style",
                      action="store_false", default=True,
                      help="Do not run the code style (PEP8) checks.")
    parser.add_option("--cython-only", dest="cython_only",
                      action="store_true", default=False,
                      help="only compile pyx to c, do not run C compiler or run the tests")
    parser.add_option("--no-refnanny", dest="with_refnanny",
                      action="store_false", default=True,
                      help="do not regression test reference counting")
    parser.add_option("--no-fork", dest="fork",
                      action="store_false", default=True,
                      help="do not fork to run tests")
    parser.add_option("--sys-pyregr", dest="system_pyregr",
                      action="store_true", default=False,
                      help="run the regression tests of the CPython installation")
    parser.add_option("-x", "--exclude", dest="exclude",
                      action="append", metavar="PATTERN",
                      help="exclude tests matching the PATTERN")
    parser.add_option("-j", "--shard_count", dest="shard_count", metavar="N",
                      type=int, default=1,
                      help="shard this run into several parallel runs")
    parser.add_option("--shard_num", dest="shard_num", metavar="K",
                      type=int, default=-1,
                      help="test only this single shard")
    parser.add_option("--profile", dest="profile",
                      action="store_true", default=False,
                      help="enable profiling of the tests")
    parser.add_option("-C", "--coverage", dest="coverage",
                      action="store_true", default=False,
                      help="collect source coverage data for the Compiler")
    parser.add_option("--coverage-xml", dest="coverage_xml",
                      action="store_true", default=False,
                      help="collect source coverage data for the Compiler in XML format")
    parser.add_option("--coverage-html", dest="coverage_html",
                      action="store_true", default=False,
                      help="collect source coverage data for the Compiler in HTML format")
    parser.add_option("-A", "--annotate", dest="annotate_source",
                      action="store_true", default=True,
                      help="generate annotated HTML versions of the test source files")
    parser.add_option("--no-annotate", dest="annotate_source",
                      action="store_false",
                      help="do not generate annotated HTML versions of the test source files")
    parser.add_option("-v", "--verbose", dest="verbosity",
                      action="count", default=0,
                      help="display test progress, pass twice to print test names")
    parser.add_option("-T", "--ticket", dest="tickets",
                      action="append",
                      help="a bug ticket number to run the respective test in 'tests/*'")
    parser.add_option("-3", dest="language_level",
                      action="store_const", const=3, default=2,
                      help="set language level to Python 3 (useful for running the CPython regression tests)'")
    parser.add_option("--xml-output", dest="xml_output_dir", metavar="DIR",
                      help="write test results in XML to directory DIR")
    parser.add_option("--exit-ok", dest="exit_ok", default=False,
                      action="store_true",
                      help="exit without error code even on test failures")
    parser.add_option("--failfast", dest="failfast", default=False,
                      action="store_true",
                      help="stop on first failure or error")
    parser.add_option("--root-dir", dest="root_dir", default=os.path.join(DISTDIR, 'tests'),
                      help=("Directory to look for the file based "
                            "tests (the ones which are deactivated with '--no-file'."))
    parser.add_option("--examples-dir", dest="examples_dir",
                      default=os.path.join(DISTDIR, 'docs', 'examples'),
                      help="Directory to look for documentation example tests")
    parser.add_option("--work-dir", dest="work_dir", default=os.path.join(os.getcwd(), 'TEST_TMP'),
                      help="working directory")
    parser.add_option("--cython-dir", dest="cython_dir", default=os.getcwd(),
                      help="Cython installation directory (default: use local source version)")
    parser.add_option("--debug", dest="for_debugging", default=False, action="store_true",
                      help="configure for easier use with a debugger (e.g. gdb)")
    parser.add_option("--pyximport-py", dest="pyximport_py", default=False, action="store_true",
                      help="use pyximport to automatically compile imported .pyx and .py files")
    parser.add_option("--watermark", dest="watermark", default=None,
                      help="deterministic generated by string")
    parser.add_option("--use_common_utility_dir", default=False, action="store_true")
    parser.add_option("--use_formal_grammar", default=False, action="store_true")
    parser.add_option("--test_determinism", default=False, action="store_true",
                      help="test whether Cython's output is deterministic")
    parser.add_option("--pythran-dir", dest="pythran_dir", default=None,
                      help="specify Pythran include directory. This will run the C++ tests using Pythran backend for Numpy")

    options, cmd_args = parser.parse_args(args)

    if options.with_cython and sys.version_info[0] >= 3:
        sys.path.insert(0, options.cython_dir)

    # requires glob with the wildcard.
    if sys.version_info < (3, 5) or cmd_args:
        options.code_style = False

    WITH_CYTHON = options.with_cython

    coverage = None
    if options.coverage or options.coverage_xml or options.coverage_html:
        if not WITH_CYTHON:
            options.coverage = options.coverage_xml = options.coverage_html = False
        elif options.shard_num == -1:
            print("Enabling coverage analysis")
            from coverage import coverage as _coverage
            coverage = _coverage(branch=True)
            coverage.erase()
            coverage.start()

    if options.xml_output_dir:
        shutil.rmtree(options.xml_output_dir, ignore_errors=True)

    if options.shard_count > 1 and options.shard_num == -1:
        import multiprocessing
        pool = multiprocessing.Pool(options.shard_count)
        tasks = [(options, cmd_args, shard_num) for shard_num in range(options.shard_count)]
        errors = []
        # NOTE: create process pool before time stamper thread to avoid forking issues.
        total_time = time.time()
        stats = Stats()
        with time_stamper_thread():
            for shard_num, shard_stats, return_code in pool.imap_unordered(runtests_callback, tasks):
                if return_code != 0:
                    errors.append(shard_num)
                    sys.stderr.write("FAILED (%s/%s)\n" % (shard_num, options.shard_count))
                sys.stderr.write("ALL DONE (%s/%s)\n" % (shard_num, options.shard_count))
                stats.update(shard_stats)
        pool.close()
        pool.join()
        total_time = time.time() - total_time
        sys.stderr.write("Sharded tests run in %d seconds (%.1f minutes)\n" % (round(total_time), total_time / 60.))
        if errors:
            sys.stderr.write("Errors for shards %s\n" % ", ".join([str(e) for e in errors]))
            return_code = 1
        else:
            return_code = 0
    else:
        with time_stamper_thread():
            _, stats, return_code = runtests(options, cmd_args, coverage)

    if coverage:
        if options.shard_count > 1 and options.shard_num == -1:
            coverage.combine()
        coverage.stop()

    stats.print_stats(sys.stderr)
    if coverage:
        save_coverage(coverage, options)

    sys.stderr.write("ALL DONE\n")
    sys.stderr.flush()

    try:
        check_thread_termination(ignore_seen=False)
    except PendingThreadsError:
        # normal program exit won't kill the threads, do it the hard way here
        flush_and_terminate(return_code)
    else:
        sys.exit(return_code)


@contextmanager
def time_stamper_thread(interval=10):
    """
    Print regular time stamps into the build logs to find slow tests.
    @param interval: time interval in seconds
    """
    try:
        _xrange = xrange
    except NameError:
        _xrange = range

    import threading
    from datetime import datetime
    from time import sleep

    interval = _xrange(interval * 4)
    now = datetime.now
    write = sys.__stderr__.write
    stop = False

    def time_stamper():
        while True:
            for _ in interval:
                if stop:
                    return
                sleep(1./4)
            write('\n#### %s\n' % now())

    thread = threading.Thread(target=time_stamper, name='time_stamper')
    thread.setDaemon(True)  # Py2.6 ...
    thread.start()
    try:
        yield
    finally:
        stop = True
        thread.join()


def configure_cython(options):
    global CompilationOptions, pyrex_default_options, cython_compile
    from Cython.Compiler.Main import \
        CompilationOptions, \
        default_options as pyrex_default_options
    from Cython.Compiler.Options import _directive_defaults as directive_defaults
    from Cython.Compiler import Errors
    Errors.LEVEL = 0  # show all warnings
    from Cython.Compiler import Options
    Options.generate_cleanup_code = 3  # complete cleanup code
    from Cython.Compiler import DebugFlags
    DebugFlags.debug_temp_code_comments = 1
    pyrex_default_options['formal_grammar'] = options.use_formal_grammar
    if options.profile:
        directive_defaults['profile'] = True
    if options.watermark:
        import Cython.Compiler.Version
        Cython.Compiler.Version.watermark = options.watermark


def save_coverage(coverage, options):
    if options.coverage:
        coverage.report(show_missing=0)
    if options.coverage_xml:
        coverage.xml_report(outfile="coverage-report.xml")
    if options.coverage_html:
        coverage.html_report(directory="coverage-report-html")


def runtests_callback(args):
    options, cmd_args, shard_num = args
    options.shard_num = shard_num
    return runtests(options, cmd_args)


def runtests(options, cmd_args, coverage=None):

    WITH_CYTHON = options.with_cython
    ROOTDIR = os.path.abspath(options.root_dir)
    WORKDIR = os.path.abspath(options.work_dir)

    if WITH_CYTHON:
        configure_cython(options)

    xml_output_dir = options.xml_output_dir
    if options.shard_num > -1:
        WORKDIR = os.path.join(WORKDIR, str(options.shard_num))
        if xml_output_dir:
            xml_output_dir = os.path.join(xml_output_dir, 'shard-%03d' % options.shard_num)

    # RUN ALL TESTS!
    UNITTEST_MODULE = "Cython"
    UNITTEST_ROOT = os.path.join(os.path.dirname(__file__), UNITTEST_MODULE)
    if WITH_CYTHON:
        if os.path.exists(WORKDIR):
            for path in os.listdir(WORKDIR):
                if path in ("support", "Cy3"): continue
                shutil.rmtree(os.path.join(WORKDIR, path), ignore_errors=True)
    if not os.path.exists(WORKDIR):
        os.makedirs(WORKDIR)

    if options.shard_num <= 0:
        sys.stderr.write("Python %s\n" % sys.version)
        sys.stderr.write("\n")
        if WITH_CYTHON:
            sys.stderr.write("Running tests against Cython %s\n" % get_version())
        else:
            sys.stderr.write("Running tests without Cython.\n")

    if options.for_debugging:
        options.cleanup_workdir = False
        options.cleanup_sharedlibs = False
        options.fork = False
        if WITH_CYTHON and include_debugger:
            from Cython.Compiler.Main import default_options as compiler_default_options
            compiler_default_options['gdb_debug'] = True
            compiler_default_options['output_dir'] = os.getcwd()

    if IS_PYPY:
        if options.with_refnanny:
            sys.stderr.write("Disabling refnanny in PyPy\n")
            options.with_refnanny = False

    if options.with_refnanny:
        from pyximport.pyxbuild import pyx_to_dll
        libpath = pyx_to_dll(os.path.join("Cython", "Runtime", "refnanny.pyx"),
                             build_in_temp=True,
                             pyxbuild_dir=os.path.join(WORKDIR, "support"))
        sys.path.insert(0, os.path.split(libpath)[0])
        CFLAGS.append("-DCYTHON_REFNANNY=1")

    if xml_output_dir and options.fork:
        # doesn't currently work together
        sys.stderr.write("Disabling forked testing to support XML test output\n")
        options.fork = False

    if WITH_CYTHON:
        sys.stderr.write("Using Cython language level %d.\n" % options.language_level)

    test_bugs = False
    if options.tickets:
        for ticket_number in options.tickets:
            test_bugs = True
            cmd_args.append('ticket:%s' % ticket_number)
    if not test_bugs:
        for selector in cmd_args:
            if selector.startswith('bugs'):
                test_bugs = True

    selectors = [ string_selector(r) for r in cmd_args ]
    verbose_excludes = selectors or options.verbosity >= 2
    if not selectors:
        selectors = [ lambda x, tags=None: True ]

    # Check which external modules are not present and exclude tests
    # which depends on them (by prefix)

    missing_dep_excluder = MissingDependencyExcluder(EXT_DEP_MODULES)
    version_dep_excluder = VersionDependencyExcluder(VER_DEP_MODULES)
    exclude_selectors = [missing_dep_excluder, version_dep_excluder] # want to print msg at exit

    try:
        import IPython.core.release
        if list(IPython.core.release._ver) < [1, 0, 0]:
            raise ImportError
    except (ImportError, AttributeError, TypeError):
        exclude_selectors.append(RegExSelector('IPython'))

    try:
        raise ImportError("Jedi typer is currently broken, see GH#1845")
        import jedi
        if not ([0, 9] <= list(map(int, re.findall('[0-9]+', jedi.__version__ or '0')))):
            raise ImportError
    except (ImportError, AttributeError, TypeError):
        exclude_selectors.append(RegExSelector('Jedi'))

    if options.exclude:
        exclude_selectors += [ string_selector(r) for r in options.exclude ]

    if not COMPILER_HAS_INT128 or not IS_CPYTHON:
        exclude_selectors += [RegExSelector('int128')]

    if options.shard_num > -1:
        exclude_selectors.append(ShardExcludeSelector(options.shard_num, options.shard_count))

    if not test_bugs:
        bug_files = [
            ('bugs.txt', True),
            ('pypy_bugs.txt', IS_PYPY),
            ('windows_bugs.txt', sys.platform == 'win32'),
            ('cygwin_bugs.txt', sys.platform == 'cygwin')
        ]

        exclude_selectors += [
            FileListExcluder(os.path.join(ROOTDIR, bugs_file_name),
                             verbose=verbose_excludes)
            for bugs_file_name, condition in bug_files if condition
        ]

    global COMPILER
    if options.compiler:
        COMPILER = options.compiler

    selected_backends = [ name.strip() for name in options.backends.split(',') if name.strip() ]
    backends = []
    for backend in selected_backends:
        if backend == 'c' and not options.use_c:
            continue
        elif backend == 'cpp' and not options.use_cpp:
            continue
        elif backend not in BACKENDS:
            sys.stderr.write("Unknown backend requested: '%s' not one of [%s]\n" % (
                backend, ','.join(BACKENDS)))
            sys.exit(1)
        backends.append(backend)
    if options.shard_num <= 0:
        sys.stderr.write("Backends: %s\n" % ','.join(backends))
    languages = backends

    if 'TRAVIS' in os.environ and sys.platform == 'darwin' and 'cpp' in languages:
        bugs_file_name = 'travis_macos_cpp_bugs.txt'
        exclude_selectors += [
            FileListExcluder(os.path.join(ROOTDIR, bugs_file_name),
                             verbose=verbose_excludes)
        ]

    if options.use_common_utility_dir:
        common_utility_dir = os.path.join(WORKDIR, 'utility_code')
        if not os.path.exists(common_utility_dir):
            os.makedirs(common_utility_dir)
    else:
        common_utility_dir = None

    sys.stderr.write("\n")

    test_suite = unittest.TestSuite()
    stats = Stats()

    if options.unittests:
        collect_unittests(UNITTEST_ROOT, UNITTEST_MODULE + ".", test_suite, selectors, exclude_selectors)

    if options.doctests:
        collect_doctests(UNITTEST_ROOT, UNITTEST_MODULE + ".", test_suite, selectors, exclude_selectors)

    if options.filetests and languages:
        filetests = TestBuilder(ROOTDIR, WORKDIR, selectors, exclude_selectors,
                                options, options.pyregr, languages, test_bugs,
                                options.language_level, common_utility_dir,
                                options.pythran_dir, add_embedded_test=True, stats=stats)
        test_suite.addTest(filetests.build_suite())
    if options.examples and languages:
        for subdirectory in glob.glob(os.path.join(options.examples_dir, "*/")):
            filetests = TestBuilder(subdirectory, WORKDIR, selectors, exclude_selectors,
                                    options, options.pyregr, languages, test_bugs,
                                    options.language_level, common_utility_dir,
                                    options.pythran_dir,
                                    default_mode='compile', stats=stats)
            test_suite.addTest(filetests.build_suite())

    if options.system_pyregr and languages:
        sys_pyregr_dir = os.path.join(sys.prefix, 'lib', 'python'+sys.version[:3], 'test')
        if not os.path.isdir(sys_pyregr_dir):
            sys_pyregr_dir = os.path.join(os.path.dirname(sys.executable), 'Lib', 'test')  # source build
        if os.path.isdir(sys_pyregr_dir):
            filetests = TestBuilder(ROOTDIR, WORKDIR, selectors, exclude_selectors,
                                    options, True, languages, test_bugs,
                                    sys.version_info[0], common_utility_dir, stats=stats)
            sys.stderr.write("Including CPython regression tests in %s\n" % sys_pyregr_dir)
            test_suite.addTest(filetests.handle_directory(sys_pyregr_dir, 'pyregr'))

    if options.code_style and options.shard_num <= 0:
        try:
            import pycodestyle
        except ImportError:
            # Hack to make the exclusion visible.
            missing_dep_excluder.tests_missing_deps.append('TestCodeFormat')
        else:
            test_suite.addTest(TestCodeFormat(options.cython_dir))

    if xml_output_dir:
        from Cython.Tests.xmlrunner import XMLTestRunner
        if not os.path.exists(xml_output_dir):
            try:
                os.makedirs(xml_output_dir)
            except OSError:
                pass  # concurrency issue?
        test_runner = XMLTestRunner(output=xml_output_dir,
                                    verbose=options.verbosity > 0)
        if options.failfast:
            sys.stderr.write("--failfast not supported with XML runner\n")
    else:
        text_runner_options = {}
        if options.failfast:
            if sys.version_info < (2, 7):
                sys.stderr.write("--failfast not supported with Python < 2.7\n")
            else:
                text_runner_options['failfast'] = True
        test_runner = unittest.TextTestRunner(verbosity=options.verbosity, **text_runner_options)

    if options.pyximport_py:
        from pyximport import pyximport
        pyximport.install(pyimport=True, build_dir=os.path.join(WORKDIR, '_pyximport'),
                          load_py_module_on_import_failure=True, inplace=True)

    try:
        gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
    except AttributeError:
        pass  # not available on PyPy

    result = test_runner.run(test_suite)

    if common_utility_dir and options.shard_num < 0 and options.cleanup_workdir:
        shutil.rmtree(common_utility_dir)

    if missing_dep_excluder.tests_missing_deps:
        sys.stderr.write("Following tests excluded because of missing dependencies on your system:\n")
        for test in missing_dep_excluder.tests_missing_deps:
            sys.stderr.write("   %s\n" % test)

    if options.with_refnanny:
        import refnanny
        sys.stderr.write("\n".join([repr(x) for x in refnanny.reflog]))

    if options.exit_ok:
        return options.shard_num, stats, 0
    else:
        return options.shard_num, stats, not result.wasSuccessful()


if __name__ == '__main__':
    try:
        main()
    except Exception:
        traceback.print_exc()
        try:
            check_thread_termination(ignore_seen=False)
        except PendingThreadsError:
            # normal program exit won't kill the threads, do it the hard way here
            flush_and_terminate(1)
        sys.exit(1)
