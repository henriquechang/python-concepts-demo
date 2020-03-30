import functools

from functools import singledispatch
from collections import abc
import numbers

@functools.lru_cache()
def fibonacci(n):
    print(n)
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


def test():
    print(fibonacci(6))


@singledispatch
def showtype(obj):
    return 'other type'


@showtype.register(str)
def _(text):
    return 'is text'


@showtype.register(numbers.Integral)
def _(n):
    return 'is num'


@showtype.register(tuple)
@showtype.register(abc.MutableSequence)
def _(seq):
    return 'is tuple'
