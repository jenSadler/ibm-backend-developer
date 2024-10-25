"""
Small program to add two numbers
"""

# Define a function named 'add' that takes two arguments, 'number1' and 'number2'.
def add(number1, number2):
    """ The function returns the sum of 'number1' and 'number2'."""
    return number1 + number2

# Initialize the variable 'num1' with the value 4.
NUM_1 = 4

# Initialize the variable 'num2' with the value 5.
NUM_2 = 5

# Call the 'add' function with 'num1' and 'num2' as arguments and store the result in 'total'.
TOTAL = add(NUM_1, NUM_2)

# Print the result of adding 'num1' and 'num2'
# using the 'format' method to insert the values into the string.
print(f"The sum of {NUM_1} and {NUM_2} is {TOTAL}")
