"""
Use the input() function to ask the user for their name. Store the result in a variable called user_name. The prompt message inside input() should be "What is your name? ".
Create a new variable called personal_greeting.
Assign a greeting string to personal_greeting that includes the user_name. For example, if the user enters "Alice", the personal_greeting should be "Hello, Alice!".
Print the personal_greeting.
"""

user_name = input("What is your name? ")
personal_greeting = f"Hello {user_name}"
print(personal_greeting)