"""
Write a decorator which wraps functions to log function arguments and the return value on each call.
Provide support for both positional and named arguments (your wrapper function should take both
*args and **kwargs and print them both):
# >>> @logged
# ... def func(*args):
# ...     return 3 + len(args)
# >>> func(4, 4, 4)
you called func(4, 4, 4)
it returned 6
6
"""


def logged(func):
    def wrapper(*args, **kwargs):
        print('you called {}{}'.format(func.__name__, args))
        result = func(*args, *kwargs)
        print('it returned {}'.format(result))
        return result
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))