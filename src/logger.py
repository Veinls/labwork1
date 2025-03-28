import time

def logger(func):
    def wrapper(*arg, **kwarg):
        start_time = time.time()
        result = func(*arg, **kwarg)
        finish_time = time.time()
        print(f'name function:{func.__name__}')
        if arg:
            print(arg)
        if kwarg:
            print(kwarg)
        return result
    return wrapper
