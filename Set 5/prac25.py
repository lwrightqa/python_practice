"""

Create an empty list called user_entries.
Start a while True: loop (an infinite loop that you will break out of).
Inside the loop:
Ask the user to enter some text using the prompt: "Enter some text (or type 'quit' to stop): ". Store this input in a variable.
Check if the user's input, when converted to lowercase, is exactly equal to the string "quit".
If it is "quit", use the break statement to exit the loop.
If it's not "quit", append the original user input (before converting to lowercase for the check) to the user_entries list.
After the loop finishes, print the user_entries list.

"""

user_entries = []

while True:
    user_input = input("Enter some text (or type 'quit' to stop): ")
    if user_input.lower() == "quit":
        break # Use break statement to exit the loop.
    else:
        user_entries.append(user_input) # Append the original user input to the user_entries list.

print(user_entries) # Print the user_entries list after the loop finishes.