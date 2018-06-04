def a_new_decorator(a_func):
    def wrapTheFunction():
        print('бла бла перед исполнением a_func()')

        a_func()

        print(',kf ,kf после исполнения fa_func()')

    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    print('Я функция, которая требует декораци')

print(a_function_requiring_decoration.__name__)

# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# a_function_requiring_decoration
