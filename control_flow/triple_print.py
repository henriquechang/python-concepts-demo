import sys
from contextlib import contextmanager


@contextmanager
def triple_print():
    original_num = sys.stdout.write

    def triple_num(value):
        original_num(value * 3)
    sys.stdout.write = triple_num
    yield 7
    sys.stdout.write = original_num
