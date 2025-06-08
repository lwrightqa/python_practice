"""
You'll be using a function similar to the is_positive function you just wrote.
Create an empty list called positive_numbers_entered.
Write a loop that asks the user to enter 3 numbers, one at a time.
Inside the loop, for each number entered:
Prompt the user with something like "Enter a number: ".
Convert the input to an integer.
Call your is_positive function with this number.
If the is_positive function returns True for the number, append that number to your positive_numbers_entered list.
After the loop has finished (i.e., after the user has entered all 3 numbers), print the positive_numbers_entered list.
Finally, print how many positive numbers were collected (i.e., the length of the positive_numbers_entered list).
You can print it like: "You entered X positive numbers." where X is the count.
"""

def is_positive(number):
    return number > 0

positive_numbers_entered = []

for i in range(3):
    number_str = input("Enter a number: ")
    number_int = int(number_str)
    if is_positive(number_int):
        positive_numbers_entered.append(number_int)

print(positive_numbers_entered)
print(f"You entered {len(positive_numbers_entered)} positive numbers.")