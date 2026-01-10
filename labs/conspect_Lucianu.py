# 0. Типы данных в Python

# Pthon сделал Гвидо Ван Россум.
# JS сделал Брендан Эйх
# C++ сделал Бьёрн Стауструп
# Pascal сделал Клаус Вирт
# C# сделала группа Microsoft с Андерсом Хейлсбергом
# Java сделал Джеймс Гослинг
# Go сделал Кен Томпсон
# Rust сделал Грейдон Хор

# Неизменяемые (немутабельные, immutable) типы данных: None, bool, int, float, complex, str, tuple. Также bytes и frozenset;
# Изменяемые (мутабельные, muttable) типы данных: list, dict, set. Также
# байтовый массив bytearray;

# 1. Именованные кортежи

from operator import mul
from functools import reduce
import weakref
import array
import builtins
import collections
import locale
import re
import sys
import typing
from collections import ChainMap, abc
from dataclasses import dataclass, field
from enum import Enum, auto
from unicodedata import normalize

import pyuca

Card = collections.namedtuple('Card', ['rank', 'suit'])

# -------------------------------------------

# 2. Дандеры
# пример для работы len и индексации скобками
# http://docs.python.org/3/reference/datamodel.html


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()


def __init__(self):
    self._cards = [Card(rank, suit) for suit in self.suits
                   for rank in self.ranks]


def __len__(self):
    return len(self._cards)


def __getitem__(self, position):
    return self._cards[position]

# -------------------------------------------

# 3. __repr__ для отладки, __str__ для визуального представления.
# строка repr должна быть годна для eval, обычно, выводит конструктор.


mydate = datetime.datetime.now()

print("str() string: ", str(mydate))
print("repr() string: ", repr(mydate))

# str() string:  2023-01-27 09:50:37.429078
# __repr__() string:  datetime.datetime(2023, 1, 27, 9, 50, 37, 429)

# -------------------------------------------

# 4. Модель данных лежит в collections.abc.


issubclass(tuple, abc.Sequence)
issubclass(list, abc.MutableSequence)

# -------------------------------------------

# 5. Последовательности
# - контейнеры: list,	 tuple	и collections.deque
# - плоские (состоят из элементов одного типа): str,  bytes и array.array

# -------------------------------------------

# 6 Генераторные выражения
# - есть списковые и картежные

# Внутри списковых включений есть локальная область видимости для переменных

x = 'ABC'
codes = [last := ord(c) for c in x]
# lst видима и после этой строки

# они могут всё то же, что и map и filter

symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))

# Списковым включением можно построить декартово произведение:

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]

# -------------------------------------------

# 7. Генераторные выражения экономят память

symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols)


array.array('I', (ord(symbol) for symbol in symbols))

# Декартово произведение генератором:
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)

# -------------------------------------------

# 8. Кортежи неизменяемые, но ключами могут быть только если внутри них
# так же неизменяемые элементы:


def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

# -------------------------------------------


# 9. Кортеж можно распаковать как в параметрах функции, так и при возврате
t = (2, 4)
quotient, remainder = divmod(*t)

# и можно использовапть rest

a, b, *rest = range(5)
a, *body, c, d = range(5)

# В функциях тоже


def fun(a, b, c, d, *rest):
    return a, b, c, d, rest


# И в списковых включениях:
[*range(4), 4]
{*range(4), 4, *(5, 6, 7)}

# -------------------------------------------

# 10. Распаковка вложенных объектов
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

for name, _, _, (lat, lon) in metro_areas:
    pass

# -------------------------------------------

# 11. Сопоставление образцам:


def handle_command(self, message):
    match message:
        case ['BEEPER', frequency, times]:
            self.beep(times, frequency)
        case ['NECK', angle]:
            self.rotate_neck(angle)
        case ['LED', ident, intensity]:
            self.leds[ident].set_brightness(ident, intensity)
        case ['LED', ident, red, green, blue]:
            self.leds[ident].set_color(ident, red, green, blue)
        case _:
            raise InvalidCommand(message)

# Возможно сопоставление с условием:
  # case [name, _, _, (lat, lon)] if lon <= 0:

# rest:
  # case ['1', *rest]

# привязка к переменной:
  # case [name, _, _, (lat, lon) as coord]

# специфичность образца по типу данных:
  # case [str(name), _, _, (float(lat), float(lon))]

# использование произвольной последовательности:
  # case [str(name), *_, (float(lat), float(lon))]:
  # тут она начинается с str и заканчивается float


# ещё пример:
record = ...
match record:
    case [name, _, _, (lat, lon)] if lon <= 0:
        print(f'{name:15} | {lat: 9.4f} | {lon: 9.4f}')

# 12. Отрицательный шаг срезов и именование срезов

s = ...
s[::-1]

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)

# присваивание срезам:
l = ...
l[2:5] = [20, 30]
del l[5:7]
l[3::2] = [11, 22]

# 13. Создать список списков
board = [['_'] * 3 for i in range(3)]

# [['_'] * 3] * 3 - так нельзя

# 14. Составное присваивание

"""
l = [1, 2, 3]
id(l)
    4311953800
l *= 2
l
[1, 2, 3, 1, 2, 3]
id(l)
4311953800

# С кортежем объект в переменной будет новый

>>> t = (1, 2, 3) >>> id(t)
4312681568  >>> t *= 2 >>> id(t) 4301348296
"""

# 15. Картеж можно поменять
t = (1, 2, [30, 40])
t[2].extend([50, 60])
print(t)

# но не так:
t[2] += [50, 60]

# 16.
# Если нужно хранить очень много скалярных велечин, например, коллекция чисел, то array лучше list.
# list хорош, когда элементы разные. А если нужно много удалять и добавлять элементов с конца или
# начала, то эффективнее deque.
#

# 17. dict и set не упорядочены, но есть OrderedDict в collections.
# Так же, можно поставить модуль pip install ordered_set: from ordered_set
# import OrderedSet.

# 18. Отсортировать массив можно только так
# a = array.array(a.typecode, sorted(a)). А поддержать ордер при вставке
# так: bisect.insort.
#
# https://www.fluentpython.com/extra/ordered-sequences-with-bisect/

# 19. Очереди: from collections import deque. У неё append и popleft атомарны.
# это позволяет делать потокобезопасную LIFO очередь.
# так же queue: Queue,	LifoQueueи  PriorityQueue
# asyncio: Queue, LifoQueue, PriorityQueue и JoinableQueue.

# 20. Последовательности: изменяемые (list) и неизменяемые (tuple),
# плоские (array) и контейнерные (list).

# 21. Кортеж можно изменить положив в элемент list. Проверить через hash.

# 22. Списковые включения (list comprehensions) и генераторные выражения
# (generator expressions) - важны.

# 23. О сортировке https://docs.python.org/3/howto/sorting.html.

# 24. Comprehensions есть списочные, словарные и множества.
"""
    List Comprehensions
    Dictionary Comprehensions
    Set Comprehensions
    Generator Comprehensions
"""

c1 = [v for v in range(21) if v % 2]
print(type(c1), c1)

c2 = {v for v in range(21) if v % 2}
print(type(c2), c2)

c3 = (v for v in range(21) if v % 2)
print(type(c3), list(c3))

c4 = {i: v for i, v in enumerate(v for v in range(21) if v % 2)}
print(type(c4), c4)

# 25. match работает со словарями


def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')


# 26. Хэшируемость
# Должен быть определён __hash__() и __eq()__ и истинность совпадать.
"""
    На  практике	 это	 требование	 означает,	 что	 методы	 __eq__()
    и  __hash__()	 должны	 принимать	 во	 внимание	 только	 те	 атрибуты
    экземпляра,	которые	не изменяются	на	протяжении	всей	жизни	объекта.
"""

# 27. Встроенные словари: dict,	 defaultdict	и OrderedDict

WORD_RE = re.compile(r'\w+')
index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

# или можно так
index = collections.defaultdict(list)
# затем:
index[word].append(location)
# поведение зашито в __missing__

# 28. Словари
collections.OrderedDict

collections.ChainMap


pylookup = ChainMap(locals(), globals(), vars(builtins))

collections.Counter
shelve.Shelf
# rUserDict - базовый класс для расширения.

# 29. Делаем словарь, приводящий ключи к строке


class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

# 30. Неизменяемые коллекции
    d = {1: 'A'}
    d_proxy = MappingProxyType(d)  # для словарей
    frozenset  # для множеств


# 31. Порядок элементов
# Множество set не сохраняет, хотя есть внешние пакеты: OrderedSet.
# dict сохраняет, и можно применять множество ключей.
l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
dict.fromkeys(l).keys()

# 32. Множества
# Элементы должны быть хешируемыми и реализовывать __hash__ и __eq__.
# frozenset хэшируем, а set - нет. Поэтому, первый можно положить в set.
# создание множества литералом: {1, 2, 3}, но пустое так не создать, надо set()
# {} - создаёт словарь

# 33. Байты bytes, bytearray и юникод
# В юникоде есть id символа и его байтовое представление.

# Преобразование  из      кодовых позиций в байты называется
# кодированием,   пре-образование        из      байтов  в кодовые
# позиции –       декодированием.

# id --> bytes  это кодирование (encode), bytes --> id декодирование (decode)
s = 'café'
len(s)
# 4
b = s.encode('utf8')  # b'caf\xc3\xa9'
# bytes и bytesarray собержат байты. Это одно и то же, второй мутабельный.
# получить байты из str:
cafe = bytes('café', encoding='utf_8')

# 34. При декодировании лучше всегда использовать кодек  UTF-8-SIG, он правильно работает с
# BOM и без него.
#
# При кодировании лучше UTF-8.
open('cafe.txt', 'w', encoding='utf_8').write('café')
# тут тоже надо задать utf_8, иначе будет windows 1251.
open('cafe.txt').read()

# locale.getpreferredencoding() - очень важно, но лучше работая с файлом
# задавать явно encoding при чтении и при записи.

# 35. При сравнении юникодовых строк важно выполнять нормализацию:
# unicodedata.normalize, так как бывают модификаторы:
s1 = 'café'
s2 = 'cafe\N{COMBINING ACUTE ACCENT}'
print(s1, s2)
# ('café', 'café')
len(s1), len(s2)
# (4, 5)
s1 == s2  # False
# формы нормализации: 'NFC',	 'NFD',	'NFKC'	или	'NFKD'
# NFC - рекомендуемая форма

# 36. При сравнении ещё нужно выполнять casefold, он отличается от lower в
# некоторых кейсах, например знак мю.

# При многоязыковых строках рекомендуется nfc_equal и fold_equal.
nfc_equal('A', 'a')  # --> False
fold_equal('A', 'a')  # --> True


def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)


def fold_equal(str1, str2):
    return (
        normalize(
            'NFC',
            str1).casefold() == normalize(
            'NFC',
            str2).casefold())

# 37.  Сортировка с использованием локали


# ставим нужную локаль
my_locale = locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')

print(my_locale)

fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=locale.strxfrm)

print(sorted_fruits)

# 38. Универсальная сортировка через юникод:

#  PyUCA	(https:// pypi.python.org/pypi/pyuca/)

coll = pyuca.Collator()
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=coll.sort_key)
sorted_fruits

# str и bytes в регулярных выражениях
re_numbers_str = re.compile(r'\d+')  # ищет все цифры, например, тамильские
re_numbers_bytes = re.compile(rb'\d+')  # ищет только ascii-цифры
# второе требует байтовый аргумент
text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"
            " as 1729 = 1³ + 12³ = 9³ + 10³.")
text_bytes = text_str.encode('utf_8')

# В Win 	locale.getpreferredencoding(),	sys.getfilesystemencoding(),	sys.getdefaultencoding() - разные,
# а в Linux utf-8.

# 39. Работа с файлом

# Должна выполняться через сендвич:
#   bytes --> str
#   обработка текста
#   str --> bytes

#  «Unicode	 HOWTO»	 (https://docs.python.org/3/howto/unicode.html)
#  «Unconfusing	Unicode: WhatIs  Unicode?»	 (https://regebro.wordpress.com/2011/03/23/unconfusing- unicode-what-is-unicode/).
# PEP     393     «Flexible       String  Representation»
# (https://www.python.org/ dev/peps/pep-0393/)


# 40. DTO - построители классов с полями, но без методов, из 3:
# collections.namedtuple
# typing.NamedTuple
# @dataclasses.dataclass

# Строим такой класс:
class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
# недостаток, что надо писать __init__ и н определён правильный __repr__ и
# __eq__.
# Построители генерят __eq__, сравнивающий поля и правильную строку.


@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


# 41. Значения по-умолчанию в полях DTO


@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)  # поле со значение по-умолчанию

    all_handles  # если без типа, то это поле класса, а не экземпляра
    # через ClassVar классовому полю dataclass можно указать тип
    all_handles: ClassVar[set[str]] = set()

# тут нужно использовать фабрику, так как list изменяемый и не может быть
# дефолтным


# 42. Пример enum


class ResourceType(Enum):
    BOOK = auto()
    EBOOK = auto()
    VIDEO = auto()


# 43. Классовые паттерны поиска:
# a) простые
match x:
    case float():
        do_something_with(x)

    case [str(name), _, _, (float(lat), float(lon))]:
        ...


# б) именованные
class City(typing.NamedTuple):
    continent: str
    name: str
    country: str


cities = [
    City('Asia', 'Tokyo', 'JP'),
    City('Asia', 'Delhi', 'IN'),
    City('North America', 'Mexico City', 'MX'),
    City('North America', 'New York', 'US'),
    City('South America', 'São Paulo', 'BR'), ]


def match_asian_cities():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia'):
                results.append(city)
    return results

# 7) позиционные образцы


def match_asian_cities_pos():
    results = []
    for city in cities:
        match city:
            case City('Asia'):
                results.append(city)
    return results

# 44. Значения по-умолчанию в аргументах функции
# нельзя использовать мутируемые значения: списки, словари.
# они вычисляются один раз при загрузке модуля и становятся атрибутами функции.
# Поэтому, будут одинаковые во всех инстансах. Это отличается от JS.


class HauntedBus:

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

# это можно увидеть, проинспектировав функцию: dir(HauntedBus.__init__)
# проблема решается копированием


def __init__(self, passengers=None):
    if passengers is None:
        self.passengers = []
    else:
        self.passengers = list(passengers)


# 45. оператор del - удаляет ссылку на объект
# В Python используется подсчёт  ссылок. В Python 2 так же есть поколения для удаления замкнутых групп.
# Освобождение памяти происходит сразу при обнулении счётчика ссылок.
# Так можно проверить освобождение памяти:

# import weakref
s1 = {1, 2, 3}
s2 = s1


def bye():
    print('...like tears in the rain.')


ender = weakref.finalize(s1, bye)
ender.alive
True
del s1
ender.alive
True
s2 = 'spam'
...like tears in the rain. >> > ender.alive
False

# 45. Особенности немутабельных типов
t1 = (1, 2, 3)
t2 = tuple(t1)
t2 is t1
True

# копирование возвращает тот же объект
# Так же, для одинаковых строк используется интернирование.

# 46. Слабые ссылки
# можно использовать для отслеживания всех инстансов класса
# WeakValueDictionary,	 WeakKeyDictionary,	 WeakSet

# 47. Передача аргументов функции, объявление
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
# позиционные / смешанные * именованные
# если нет / или *, то передача по позиции или имени
# def foo(name, **kwds) - определение с ...rest аргументом
# в kwds - словарь всех остальных параметров


# 47. !!! Модель передачи параметров в функцию !!!
# В Python всё - объекты, поэтому передаётся ссылка по значению.
# У него есть: id(val), type(val) и значение
# в Python используется модель передачи через присваивание
# (pass-by-assignment).
#
# Так же, нельзя делать так:
def foo(a, l=[]):
    l.append(a)
    return l

# 48. High order - функция - это функция, принимающая или возвращающая
# другую функцию. Но сейчас есть lambda-выражения.


# 49. Очень полезный модуль - functools и operator


def factorial(n):
    return reduce(mul, range(1, n + 1))
