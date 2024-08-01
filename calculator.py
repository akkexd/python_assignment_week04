# Define the 'add' function
def add(a, b):
    return a + b

# Define the 'subtract' function
def subtract(a, b):
    return a - b

# Define the 'multiply' function
def multiply(a, b):
    return a * b

# Define the 'divide' function
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Main block
if __name__ == "__main__":
    # Sample inputs
    x = 10
    y = 5

    # Call 'add' function
    result_add = add(x, y)
    print(f"{x} + {y} = {result_add}")

    # Call 'subtract' function
    result_subtract = subtract(x, y)
    print(f"{x} - {y} = {result_subtract}")

    # Call 'multiply' function
    result_multiply = multiply(x, y)
    print(f"{x} * {y} = {result_multiply}")

    # Call 'divide' function
    result_divide = divide(x, y)
    print(f"{x} / {y} = {result_divide}")