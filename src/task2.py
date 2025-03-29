import time

def retry(attempts, delay, exceptions=None):
    def decorator(func):
        def wrapper(*arg, **kwarg):
            last_error = None
            for attempt in range(attempts):
                try:
                    return func(*arg, **kwarg)
                except Exception as error:
                    if exceptions is not None:
                        if not isinstance(error, tuple(exceptions)):
                            raise
                        last_error = error
                        print(f"Попытка {attempt + 1}: {error}")
                        if attempt < attempts - 1:
                            time.sleep(delay)
            raise last_error
        return wrapper
    return decorator

@retry(attempts=3, delay=1, exceptions=[ZeroDivisionError])
def always_fail():
    return 1 / 0  # Всегда вызывает ZeroDivisionError

# Вызов функции
try:
    always_fail()
except ZeroDivisionError as e:
    print(f"Финальный результат: {e}")