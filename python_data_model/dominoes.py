import collections
from typing import List

Domino = collections.namedtuple('Domino', ['left', 'right'])


# This example shows that our classes don't need to use arbitary methods:
class DominoesSet:
    numbers = [str(n) for n in range(0, 7)]

    def __init__(self):
        self.dominoes = self.__create_dominoes_set()

    def __len__(self):
        return len(self.dominoes)

    def __getitem__(self, position):
        return self.dominoes[position]

    def __create_dominoes_set(self) -> List:
        domino_set = []
        for left in self.numbers:
            for right in self.numbers:
                if Domino(right, left) not in domino_set:
                    domino_set.append(Domino(left, right))
        return domino_set
