def func1(a):
    a = a + 4

    def func2(b):
        return b * a

    return func2


test_func = func1(4)

test_func(5)