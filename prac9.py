'''
Define a function named create_greeting.
This function should take one argument (also known as a parameter) called name (which you can expect to be a string).
Inside the function, it should create a greeting string. The greeting should be "Hello, name! Hope you're having a good day." (where name is replaced by the value of the name parameter).
The function should then print this greeting string to the console.
After defining the function, call it with your name (or any name) as the argument to test it.
'''

def create_greeting(name):
    greeting_message = f"Hello, {name}! Hope you're having a good day."
    print(greeting_message)

create_greeting("Lisa")