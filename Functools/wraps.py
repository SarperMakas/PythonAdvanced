from functools import wraps

def mylogger(func):

    @wraps(func) # set name and doc information same as original func
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@mylogger
def add(a, b):
    """add a and b"""
    return a + b

add(1, 2)

print(add.__name__)
print(add.__doc__)