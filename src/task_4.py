
def call_limiter(limit):
    def decorator(calls):
        class wrepped(calls):
            def __init__(self, *arg, **kwarg):
                super.__init__(*arg, **kwarg)
                self.call_counts = {}
            def __getattribute__(self, name):
                attribute = super().__getattribute__(name)
                def wrapper(*arg, **kwarg):
                    current_count = self.call_counts(name,0)
                    if current_count >= calls:
                        raise RuntimeError(f"Превышено количество вызовов метода")
                    self.call_counts[name] = current_count + 1
                    return attribute(*arg,**kwarg)
                return wrapper
        return wrepped
    return decorator()

