class ReverseSortingCage:

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
