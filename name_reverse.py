# Get user input and store it in a variable
input_str = input("What's your name? ")

# Define a function to reverse a string
def reverse_string(name):
    # Use the reversed() function to get an iterator of the string in reverse order.
    # Then, use ''.join() to concatenate the characters back into a string
    return ''.join(reversed(name))

# Call the reverse_string function with the user's input
reversed_str = reverse_string(input_str)

# Print the reversed name with a friendly message
print("It's backwards day! Your name is: " + reversed_str)