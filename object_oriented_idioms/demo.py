class Demo:
    __slots__ = ('__name')

    def __init__(self, name):
        self.__name = str(name)

    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args

    @property
    def name(self):
        return self.__name
