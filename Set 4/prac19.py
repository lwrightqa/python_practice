"""
Define a function named is_positive.
This function should take one argument: number.
Inside the function, it should check if the given number is strictly greater than 0.
The function should return True if the number is greater than 0, and False otherwise.
After defining the function, test it by:
Calling is_positive with a positive number (e.g., 10) and printing the returned result.
Calling is_positive with a negative number (e.g., -5) and printing the returned result.
Calling is_positive with 0 and printing the returned result.
"""

def is_positive(number):
    if number > 0:
        return True
    else:
        return False

print(is_positive(10))
print(is_positive(-5))
print(is_positive(0))