import bisect
import os

from collections import deque
from collections import namedtuple
from random import random
from array import array

Person = namedtuple('Person', 'name gender age')


def cartesian_product(list1: [], list2: []):
    return \
        [(item1, item2)
         for item1 in list1
         for item2 in list2
         ]


def ascii_generator(symbols: str):
    return tuple(
        ord(symbol) for symbol in symbols
    )


def unpacking_simple(latitude: int, longitude: int):
    coordinates = (latitude, longitude)
    latitude, longitude = coordinates
    return latitude, longitude


def unpacking_dummy(path: str, pack: bool):
    filename = os.path.split(path)
    if pack:
        _, filename = os.path.split(path)
    return filename


def grab_excess(num: int):
    a, b, *rest = range(num)
    return a, b, rest


def create_person(data: tuple):
    person = Person._make(data)
    return person._asdict()


def slice_simple(data, index: int, skip: bool):
    result = data[:index]
    if skip:
        result = data[::index]
    return result


def assign_to_slices(data: [], first: int, second: int, itens: []):
    data[first:second] = itens
    return data


def bisect_grade(score, breakpoints=None, grades='FDCBA'):
    if breakpoints is None:
        breakpoints = [60, 70, 80, 90]
    i = bisect.bisect(breakpoints, score)
    return grades[i]


def float_array(precision: int):
    return array('d', (
        random() for i in range(10**precision)
    ))


def memory_view_example(list: [], index: int, data: int):
    numbers = array('h', list)
    memv = memoryview(numbers)
    memv_oct = memv.cast('B')
    memv_oct.tolist()
    print(numbers)
    memv_oct[index] = data
    return numbers


def deque_extension(max: int, ext=None):
    dq = deque(range(max), maxlen=max)
    if ext:
        dq.extend(ext)
    return dq