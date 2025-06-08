""" Ask the user for their name using the prompt: "What is your name? ".
Regardless of how the user types their name (e.g., "john", "John", "JOHN"), you want to greet them as if their name is "John".
Use an if-elif-else structure:
If the user's name, when converted to lowercase, is "john", print "Hello John! Nice to see you."
Else if the user's name, when converted to lowercase, is "jane", print "Hi Jane! Welcome back."
Else, print a generic greeting: "Hello there!"
Hint: Strings have a method to convert them to all lowercase letters. You used .upper() before; look for its counterpart."""

# User Prompt
name_input = input("What is your name? ")

# Make name input lowercase.
name_lower = name_input.lower()

# Conditional Statements
if name_lower == "john":
    print("Hello John! Nice to see you.")
elif name_lower == "jane":
    print("Hello Jane! Welcome back.")
else:
    print("Hello there!")