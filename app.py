def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

if __name__ == "__main__":
    print(f"Add: {add(5, 3)}")
    print(f"Subtract: {subtract(5, 3)}")
    print(f"Multiply: {multiply(5, 3)}")
    print(f"Divide: {divide(5, 3)}")
