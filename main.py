# main.py

# Importing modules from the utilities package
from utilities.calculator import add, subtract, multiply, divide
from utilities.string_operations import reverse_string, capitalize_string, lowercase_string, uppercase_string

# Sample inputs and printing results using calculator.py
print("Using calculator.py:")
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))

# Sample strings and printing results using string_operations.py
sample_string = "hello World"
print("\nUsing string_operations.py:")
print("Original:", sample_string)
print("Reversed:", reverse_string(sample_string))
print("Capitalized:", capitalize_string(sample_string))
print("Lowercase:", lowercase_string(sample_string))
print("Uppercase:", uppercase_string(sample_string))

