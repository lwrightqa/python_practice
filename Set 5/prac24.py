"""

Define a function named square_list_elements.
This function should take one argument: numbers_list (which you can expect to be a list of numbers).
Inside the function, create a new empty list called squared_numbers.
Iterate through each number in the input numbers_list. For each number, calculate its square (number * number).
Append each calculated square to the squared_numbers list.
After iterating through all the numbers, the function should return the squared_numbers list.
After defining the function:
Create a sample list of numbers, e.g., my_numbers = [1, 2, 3, 4, 5].
Call square_list_elements with my_numbers.
Store the returned list in a new variable (e.g., result_squares).
Print the result_squares list.

"""

numbers_list = [1, 2, 3, 4, 5]

def square_list_elements(numbers):
    squared_numbers = []
    for i in numbers:
        squared_numbers.append(i ** 2)
    return squared_numbers

def main():
    result_squares = square_list_elements(numbers_list)
    print(result_squares)

if __name__ == "__main__":
    main()