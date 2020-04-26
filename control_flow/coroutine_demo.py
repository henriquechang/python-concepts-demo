from functools import wraps


def coroutine(func):
    @wraps(func)
    def primer(*args,**kwargs):
        gen = func(*args,**kwargs)
        next(gen)
        return gen
    return primer


class Result(object):

    def __init__(self, count, average):
        self.count = count
        self.average = average

    def __repr__(self):
        return 'Result(%r, %r)' % (self.count, self.average)

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)