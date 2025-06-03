"""
Ask the user to enter an integer (a whole number) using the input() function. The prompt should be, "Enter an integer: ".
Convert the user's input into an integer and store it in a variable.
Use an if-elif-else statement to determine if the number is positive, negative, or zero:
If the number is greater than 0, print "The number is positive."
Else if (elif) the number is less than 0, print "The number is negative."
Else (if it's neither greater than 0 nor less than 0), print "The number is zero."
"""

integer_number = input("Enter an integer: ")
integer_number = int(integer_number)

if integer_number > 0:
    print("The number is positive.")
elif integer_number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")