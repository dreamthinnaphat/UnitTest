def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Mutiply Function"""
    return x * y

def divide(x, y):
    """Divide Fuction"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

print(divide(10,5))