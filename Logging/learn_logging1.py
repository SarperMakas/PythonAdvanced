import logging

# DEBUG: detailed information, typically of interest only when diagnosing problem
# INFO: confirmation that things are working as expected
# WARNING: something unexpected happened
# ERROR: Serious problem
# CRITICAL: A serious error

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

filename = "test.log"
logging.basicConfig(filename=filename, level=logging.DEBUG,
                    format="%(asctime)s:%(levelname)s:%(message)s")

num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
logging.warning(f"Add: {num_1} + {num_2} = {add_result}")

sub_result = subtract(num_1, num_2)
logging.warning(f"Sub: {num_1} - {num_2} = {sub_result}")

mul_result = multiply(num_1, num_2)
logging.warning(f"Mul: {num_1} * {num_2} = {mul_result}")

div_result = divide(num_1, num_2)
logging.warning(f"Div: {num_1} : {num_2} = {div_result}")