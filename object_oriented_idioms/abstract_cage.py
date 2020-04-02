from abc import ABC, abstractmethod


class AbstractCage(ABC):

    @abstractmethod
    def pick_min(self):
        pass

    def loaded(self):
        return bool(self.__class__)


class ReverseSortingCage(AbstractCage):

    def __init__(self, items):
        self._items = list(items)
        self._items.sort(reverse=True)

    def pick_min(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Reverse Sorting Cage is Empty')

    def __call__(self):
        return self.pick_min()


class NormalSortingCage(AbstractCage):

    def __init__(self, items):
        self._items = list(items)
        self._items.sort(reverse=False)

    def pick_min(self):
        try:
            return self._items[0]
        except IndexError:
            raise LookupError('Reverse Sorting Cage is Empty')

    def __call__(self):
        return self.pick_min()