def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    #Added fix 
    if b == 0:
        return "Error: Division by zero"
    return a / b