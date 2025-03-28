import time

def retry(attempts, delay, exceptions=None):
    def decorator(func):
        def wrapper(*arg, **kwarg):
            last_error = None
            for attempt in range(attempts):
                try:
                    func(*arg, **kwarg)
                except exceptions as error:
                    if exceptions is None:
                        pass
                    elif not isinstance(error, tuple(exceptions)):
                        raise
                last_error = error
                print(f"Попытка {attempt + 1}/{attempts} ошибка: {error}")
                if attempt < attempts - 1:
                    time.sleep(delay)
            raise last_error if last_error else Exception("Все попытки исчерпаны")
        return wrapper
    return decorator

@retry(10, 2, [ZeroDivisionError])
def negr():
    return 1 / 0
