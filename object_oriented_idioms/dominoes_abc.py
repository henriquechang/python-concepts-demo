import collections
from typing import List

Domino = collections.namedtuple('Domino', ['left', 'right'])


class DominoesSet(collections.MutableSequence):
    numbers = [str(n) for n in range(0, 7)]

    def __init__(self):
        self.dominoes = self.__create_dominoes_set()

    def __len__(self):
        return len(self.dominoes)

    def __repr__(self):
        return 'Dominó(%r)' % self.dominoes

    def __bool__(self):
        return bool(self.dominoes)

    def __getitem__(self, position):
        return self.dominoes[position]

    def __setitem__(self, position, value):
        self.dominoes[position] = value

    def __delitem__(self, position):
        del self.dominoes[position]

    def insert(self, position, value):
        self.dominoes.insert(position, value)

    def __create_dominoes_set(self) -> List:
        domino_set = []
        for left in self.numbers:
            for right in self.numbers:
                if Domino(right, left) not in domino_set:
                    domino_set.append(Domino(left, right))
        return domino_set
