from assemblyline.common.classification import InvalidClassification

from assemblyline.odm import model, Model, KeyMaskException, Compound, List, \
    Keyword, Integer, Mapping, Classification, Enum

import json
import pytest
import os


class CatError(Exception):
    """A unique exception class."""
    pass


def test_index_defaults():
    @model()
    class Test1(Model):
        default = Keyword()
        indexed = Keyword(index=True)
        not_indexed = Keyword(index=False)

    fields = dict(Test1.fields())
    assert fields['default'].index is None
    assert fields['indexed'].index is True
    assert fields['not_indexed'].index is False

    @model(index=True)
    class Test2(Model):
        default = Keyword()
        indexed = Keyword(index=True)
        not_indexed = Keyword(index=False)

    fields = dict(Test2.fields())
    assert fields['default'].index is True
    assert fields['indexed'].index is True
    assert fields['not_indexed'].index is False

    @model(index=False)
    class Test3(Model):
        default = Keyword()
        indexed = Keyword(index=True)
        not_indexed = Keyword(index=False)

    fields = dict(Test3.fields())
    assert fields['default'].index is False
    assert fields['indexed'].index is True
    assert fields['not_indexed'].index is False


def test_compound_index_defaults():
    @model()
    class SubModel(Model):
        default = Keyword()
        indexed = Keyword(index=True)
        not_indexed = Keyword(index=False)

    @model()
    class Test1(Model):
        default = Compound(SubModel)
        indexed = Compound(SubModel, index=True)
        not_indexed = Compound(SubModel, index=False)

    fields = Test1.flat_fields()
    assert fields['default.default'].index is None
    assert fields['default.indexed'].index is True
    assert fields['default.not_indexed'].index is False

    fields = Test1.flat_fields()
    assert fields['indexed.default'].index is True
    assert fields['indexed.indexed'].index is True
    assert fields['indexed.not_indexed'].index is False

    fields = Test1.flat_fields()
    assert fields['not_indexed.default'].index is False
    assert fields['not_indexed.indexed'].index is True
    assert fields['not_indexed.not_indexed'].index is False


def test_creation():
    @model()
    class Test(Model):
        first = Keyword()
        second = Integer()

    instance = Test(dict(first='abc', second=567))

    assert instance.first == 'abc'
    assert instance.second == 567

    instance.first = 'xyz'
    instance.second = 123

    assert instance.first == 'xyz'
    assert instance.second == 123


def test_type_validation():
    @model()
    class Test(Model):
        first = Keyword()
        second = Integer()

    with pytest.raises(ValueError):
        Test(dict(cats=123))

    instance = Test(dict(first='abc', second=567))

    with pytest.raises(ValueError):
        instance.second = 'cats'


# noinspection PyPropertyAccess
def test_setters():
    # noinspection PyPropertyDefinition
    @model()
    class Test(Model):
        first = Keyword()

        @first.setter
        def first(self, value):
            assert isinstance(value, str)
            if value.startswith('cat'):
                raise CatError()
            return value

    instance = Test(dict(first='abc'))
    assert instance.first == 'abc'

    instance.first = 'xyz'
    assert instance.first == 'xyz'

    instance.first = 123
    assert instance.first == '123'

    with pytest.raises(CatError):
        instance.first = 'cats'


def test_setters_side_effects():
    """Test setters that change other field values."""

    # noinspection PyPropertyAccess, PyPropertyDefinition
    @model()
    class Test(Model):
        a = Integer()
        b = Integer()
        best = Integer()

        @a.setter
        def a(self, value):
            self.best = min(self.b, value)
            return value

        @b.setter
        def b(self, value):
            self.best = min(self.a, value)
            return value

    instance = Test(dict(a=-100, b=10, best=-100))

    instance.a = 50
    assert instance.best == 10
    instance.b = -10
    assert instance.best == -10


# noinspection PyPropertyAccess
def test_getters():
    # noinspection PyPropertyDefinition
    @model()
    class Test(Model):
        first = Integer()

        @first.getter
        def first(self, value):
            return value if value >= 1 else 100

    instance = Test(dict(first=10))
    assert instance.first == 10

    instance.first = -1
    assert instance.first == 100

    instance.first = 500
    assert instance.first == 500


def test_create_compound():

    @model()
    class TestCompound(Model):
        key = Keyword()
        value = Keyword()

    @model()
    class Test(Model):
        first = Compound(TestCompound)

    test = Test({'first': {'key': 'a', 'value': 'b'}})
    assert test.first.key == 'a'
    test.first.key = 100
    assert test.first.key == '100'


def test_json():

    @model()
    class Inner(Model):
        number = Integer()
        value = Keyword()

    @model()
    class Test(Model):
        a = Compound(Inner)
        b = Integer()

    a = Test(dict(b=10, a={'number': 499, 'value': 'cats'}))
    b = Test(json.loads(a.json()))

    assert b.b == 10
    assert b.a.number == 499
    assert b.a.value == 'cats'


def test_create_list():
    @model()
    class Test(Model):
        values = List(Integer())

    _ = Test(dict(values=[]))
    test = Test(dict(values=[0, 100]))

    with pytest.raises(ValueError):
        Test(dict(values=['bugs']))

    with pytest.raises(ValueError):
        Test(dict(values='bugs'))

    assert test.values[0] == 0
    assert test.values[1] == 100

    test.values.append(10)
    assert len(test.values) == 3

    with pytest.raises(ValueError):
        test.values.append('cats')

    with pytest.raises(ValueError):
        test.values[0] = 'cats'

    test.values += range(5)
    assert len(test.values) == 8

    test.values.extend(range(2))
    assert len(test.values) == 10

    test.values.insert(0, -100)
    assert len(test.values) == 11
    assert test.values[0] == -100

    test.values[0:5] = range(5)
    assert len(test.values) == 11
    for ii in range(5):
        assert test.values[ii] == ii


def test_create_list_compounds():
    @model()
    class Entry(Model):
        value = Integer()
        key = Keyword()

    @model()
    class Test(Model):
        values = List(Compound(Entry))

    fields = Test.fields()
    assert len(fields) == 1
    fields = Test.flat_fields()
    assert len(fields) == 2

    _ = Test(dict(values=[]))
    test = Test({'values': [
        {'key': 'cat', 'value': 0},
        {'key': 'rat', 'value': 100}
    ]})

    with pytest.raises(TypeError):
        Test(values=['bugs'])

    with pytest.raises(TypeError):
        Test(values='bugs')

    assert test.values[0].value == 0
    assert test.values[1].value == 100

    test.values.append({'key': 'bat', 'value': 50})

    assert len(test.values) == 3

    with pytest.raises(TypeError):
        test.values.append(1000)

    with pytest.raises(TypeError):
        test.values[0] = 'cats'

    with pytest.raises(ValueError):
        test.values[0] = {'key': 'bat', 'value': 50, 'extra': 1000}

    test.values[0].key = 'dog'


def test_defaults():

    @model()
    class InnerA(Model):
        number = Integer(default=10)
        value = Keyword()

    @model()
    class InnerB(Model):
        number = Integer()
        value = Keyword()

    @model()
    class Test(Model):
        a = Compound(InnerA)
        b = Compound(InnerB)
        c = Compound(InnerB, default={'number': 99, 'value': 'yellow'})
        x = Integer()
        y = Integer(default=-1)

    # Build a model with missing data found in the defaults
    test = Test({
        'a': {'value': 'red'},
        'b': {'number': -100, 'value': 'blue'},
        'x': -55
    })

    assert test.a.number == 10
    assert test.a.value == 'red'
    assert test.b.number == -100
    assert test.b.value == 'blue'
    assert test.c.number == 99
    assert test.c.value == 'yellow'
    assert test.x == -55
    assert test.y == -1


def test_field_masking():
    @model()
    class Test(Model):
        a = Integer()
        b = Integer()

    test = Test(dict(a=10), mask=['a'])

    assert test.a == 10

    with pytest.raises(KeyMaskException):
        _ = test.b

    with pytest.raises(KeyMaskException):
        test.b = 100


def test_sub_field_masking():
    @model()
    class Inner(Model):
        a = Integer()
        b = Integer()

    @model()
    class Test(Model):
        a = Compound(Inner)
        b = Compound(Inner)

    test = Test(dict(a=dict(a=10), b=dict(b=10)), mask=['a.a', 'b.b'])

    assert test.a.a == 10

    with pytest.raises(KeyMaskException):
        _ = test.b.a

    with pytest.raises(KeyMaskException):
        test.a.b = 100


def test_mapping():
    @model()
    class Test(Model):
        a = Mapping(Integer(), default={})

    test = Test({})

    assert len(test.a) == 0

    with pytest.raises(KeyError):
        _ = test.a['abc']

    with pytest.raises(KeyError):
        test.a['abc.abc.abc'] = None

    with pytest.raises(KeyError):
        test.a['4abc.abc.abc'] = None

    test.a['cat'] = 10
    test.a['dog'] = -100

    assert len(test.a) == 2
    assert test.a['dog'] == -100

    with pytest.raises(ValueError):
        test.a['red'] = 'can'

    test = Test({'a': {'walk': 100}})
    assert len(test.a) == 1
    assert test.a['walk'] == 100


def test_classification():
    yml_config = os.path.join(os.path.dirname(__file__), "classification.yml")

    @model(index=True, store=True)
    class ClassificationTest(Model):
        cl = Classification(default="UNRESTRICTED", yml_config=yml_config)

    u = ClassificationTest({"cl": "U//REL TO D1, D2"})
    r = ClassificationTest({"cl": "R//GOD//REL TO G1"})

    assert str(r.cl) == "RESTRICTED//ADMIN//ANY/GROUP 1"

    assert u.cl < r.cl
    assert u.cl <= u.cl
    assert u.cl >= u.cl
    assert not u.cl >= r.cl
    assert not u.cl > u.cl
    assert u.cl == u.cl
    assert not u.cl != u.cl
    assert r.cl > u.cl
    assert not u.cl > r.cl
    assert str(u.cl.min(r.cl)) == "UNRESTRICTED//REL TO DEPARTMENT 1, DEPARTMENT 2"
    assert str(u.cl.max(r.cl)) == "RESTRICTED//ADMIN//ANY/GROUP 1"
    assert str(u.cl.intersect(r.cl)) == "UNRESTRICTED//ANY"
    assert str(r.cl.small()) == "R//ADM//ANY/G1"

    with pytest.raises(InvalidClassification):
        _ = ClassificationTest({"cl": "D//BOB//REL TO SOUP"})

    c1 = ClassificationTest({"cl": "U//REL TO D1"})
    c2 = ClassificationTest({"cl": "U//REL TO D2"})
    assert str(c1.cl.min(c2.cl)) == "UNRESTRICTED//REL TO DEPARTMENT 1, DEPARTMENT 2"
    assert str(c1.cl.intersect(c2.cl)) == "UNRESTRICTED"
    with pytest.raises(InvalidClassification):
        _ = c1.cl.max(c2.cl)


def test_enum():
    @model(index=True, store=True)
    class EnumTest(Model):
        enum = Enum(values=("magic", "solr", "elasticsearch"))

    et = EnumTest({"enum": "magic"})
    assert et.enum == "magic"

    et.enum = "magic"
    assert et.enum == "magic"
    et.enum = "solr"
    assert et.enum == "solr"
    et.enum = "elasticsearch"
    assert et.enum == "elasticsearch"

    with pytest.raises(ValueError):
        et.enum = "bob"

    with pytest.raises(ValueError):
        et.enum = "mysql"

    with pytest.raises(ValueError):
        et.enum = 1

    with pytest.raises(TypeError):
        et.enum = ["a"]

    with pytest.raises(ValueError):
        et.enum = True


# noinspection PyUnusedLocal
def test_banned_keys():
    with pytest.raises(ValueError):
        @model(index=True, store=True)
        class BannedTest(Model):
            _1 = Integer()

    with pytest.raises(ValueError):
        @model(index=True, store=True)
        class BannedTest(Model):
            id = Integer()

    with pytest.raises(ValueError):
        @model(index=True, store=True)
        class BannedTest(Model):
            ALL = Integer()


def test_named_item_access():
    @model()
    class Inner(Model):
        a = Integer()
        b = Integer()

    @model()
    class Test(Model):
        a = Compound(Inner)
        b = Integer()

    test = Test(dict(a=dict(a=10, b=100), b=99))

    assert test.a['a'] == 10
    assert test['a'].a == 10
    assert test.a.a == 10
    assert test['a']['a'] == 10
    test.a['a'] = 1
    assert test.a['a'] == 1
    assert test['a'].a == 1
    assert test.a.a == 1
    assert test['a']['a'] == 1
    test['a'].a = -1
    assert test.a['a'] == -1
    assert test['a'].a == -1
    assert test.a.a == -1
    assert test['a']['a'] == -1

    with pytest.raises(KeyError):
        _ = test['x']

    with pytest.raises(KeyError):
        test['x'] = 100

    assert test['a'] == {'a': -1, 'b': 100}