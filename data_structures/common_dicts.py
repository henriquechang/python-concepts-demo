import collections

my_dict = {}


def dict_comprehension(my_list: []):
    return {key: value for value, key in my_list}


def set_comprehension(div: int):
    return set(i for i in range(1, 99) if i % div == 0)


def set_default_example(key, value):
    return my_dict.setdefault(key, []).append(value)


class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item