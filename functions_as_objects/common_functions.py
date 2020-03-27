import json
from functools import partial
from operator import itemgetter


def dict_builder(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' {"%s": "%s"}' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = "null"
    if content:
        content_concat = ''.join('%s ' % c for c in content)
        dict_str = '{ "name": "%s", "attr_str": %s, "content": "%s" }' % (name, attr_str, content_concat)
    else:
        dict_str = '{"name": "%s"}' % name
    return json.loads(dict_str)


def sort_using_itemgetter(data: [], index: int):
    return sorted(data, key=itemgetter(index))


def use_partial_example(func, num):
    funcs = partial(func, num)
    return list(map(funcs, range(1, 10)))
