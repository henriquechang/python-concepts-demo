registry = []
b = 3


def register(should_add=True):
    def decorate(func):
        print('executado antes : (%s)' % func)
        if should_add:
            print('fucn add : (%s)' % func)
            registry.append(func)
        return func
    return decorate


@register()
def f1():
    print('rodando f1()')


@register(should_add=False)
def f2():
    print('rodando f2()')


def f3():
    print('rodando f3()')


def main():
    print('rodando main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()