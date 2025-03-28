import time

def logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        finish_time = time.time()
        print(f'name function:{func.__name__}')
        if args: print(args)
        if kwargs: print(kwargs)
        print(result)
        return result
    return wrapper
