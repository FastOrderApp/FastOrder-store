

def trying_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
            func(*args, **kwargs)
    return wrapper

def decorate_log(func):
    def wrapper(*args, **kwargs):
        # print(f"Function {func.__name__} called with args: {args}, kwargs: {kwargs}")
        print(f"Function {func.__name__} called")
        func(*args, **kwargs)
        print(f"Function {func.__name__} finished")
    return wrapper