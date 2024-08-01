
add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b if b != 0 else "Error: Division by zero"

# Main bloc
if __name__ == "__main__":
    # Sample inputs
    x = 10
    y = 5

    # Call lambda functions
    result_add = add(x, y)
    print(f"{x} + {y} = {result_add}")

    result_subtract = subtract(x, y)
    print(f"{x} - {y} = {result_subtract}")

    result_multiply = multiply(x, y)
    print(f"{x} * {y} = {result_multiply}")

    result_divide = divide(x, y)
    print(f"{x} / {y} = {result_divide}")
