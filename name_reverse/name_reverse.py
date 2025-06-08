# Define a function to reverse a string
def reversed_string(name):
    # Use the reversed() function to get an iterator of the string in reverse order.
    # Then, use ''.join() to concatenate the characters back into a string
    return ''.join(reversed(name))

# This block runs ONLY when name_reverse.py is executed directly
if __name__ == "__main__":
    input_str = input("What's your name? ")
    reversed_str = reversed_string(input_str)
    print(f"It's backwards day! Your name is: {reversed_str}")