import itertools


class GeometricProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        if self.step == 0 or self.begin == 0:
            return
        while forever or index < self.end:
            yield result
            index += 1
            if index == 0:
                result = self.begin * self.step
            else:
                result = result * self.step
