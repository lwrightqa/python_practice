"""
Ask the user to enter a whole number using the input() function. The prompt should be "Enter a whole number: ".
Convert the user's input (which will be a string) into an integer and store it in a variable called number.
Use an if-else statement to check the value of number:
If number is greater than 10, print the message "That's a big number!".
Otherwise (if it's 10 or less), print the message "Nice number!".
"""

number = input("Enter a whole number: ")
integer_number = int(number)

if integer_number > 10:
    print("That's a big number!")

else:
    print("Nice number!")