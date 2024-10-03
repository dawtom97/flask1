

def is_string(func):
    def wrapper(value):
        if not isinstance(value,str):
            raise TypeError("Argument musi być dypu string")
        return func(value)
    return wrapper 


def log_message(func, level):
    def decorator(func):
        def wrapper(*args):
            print(f"[{level}] Wywołanie funkcji {func.__name__}")
            return func(*args)
        return wrapper
    return decorator