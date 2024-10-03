

# def simple_decorator(func):
#     def wrapper():
#         print("Rozpoczynam działanie funkcji...")
#         func()
#         print("Kończe działanie funkcji")
#     return wrapper

# @simple_decorator
# def hello():
#     print("Witam wszystkich")

# @simple_decorator
# def another():
#     print("witam również")

# hello()
# another()

from decorators.convert_temp import convert_temp
from decorators.type_decorators import is_string, log_message

@convert_temp
def current_temp(temp):
    print(f"Temp. wynosi: {temp} C")

@is_string
def letters(message):
    print(message)

@log_message("LOW")
def test1(a,b):
    print(a + b)

test1(6,7)