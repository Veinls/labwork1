def call_limiter(limit):
    def decorator(calls):
        class wrepped(calls):
            def __init__(self, *arg, **kwarg):
                super().__init__(*arg, **kwarg)
                self._call_counts = {}
            def __getattribute__(self, name):
                attribute = super().__getattribute__(name)
                if (callable(attribute) and not name.startswith('__') and not name.endswith('__')):
                    def wrapper(*arg, **kwarg):
                        current_count = self._call_counts.get(name,0)
                        if current_count >= limit:
                            raise RuntimeError(f"Превышено количество вызовов метода")
                        self._call_counts[name] = current_count + 1
                        return attribute(*arg,**kwarg)
                    return wrapper
                return attribute
        return wrepped
    return decorator
