import time

def is_magic_method(method_name):
    return method_name.startswith('__') and method_name.endswith('__')

def logger(func, show_magic_methods=True):
    def wrapper(self, *args, **kwargs):
        if not(show_magic_methods) and is_magic_method(func.__name__):
            return None

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'class name: {self.__name__}')
        print(f'method name: {func.__name__}')
        print(f'time: {end_time - start_time}')
        print(result)

        return result
    return wrapper
