import time

def is_magic_method(method_name):
    return method_name.startswith('__') and method_name.endswith('__')

def logger(func, show_magic_methods=True):
    def wrapper(self, *args, **kwargs):
        if not(show_magic_methods) and is_magic_method(func.__name__):
            return None

        result = func(*args, **kwargs)
        print(f'class name: {self.__name__}')
        print(f'method name: {func.__name__}')
        print(result)

        return result
    return wrapper

