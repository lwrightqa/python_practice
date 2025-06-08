"""
Create a dictionary named pet_details and initialize it with the following
two key-value pairs: "type": "Dog", and "name": "Buddy"
Print the original pet_details dictionary to the console.
Now, add a new key-value pair to the pet_details dictionary: "age" should
be the key, and 3 (an integer) should be its value.
After adding the new pair, print the updated pet_details dictionary to the
console.
"""

pet_details = {
    "type": "Dog",
    "name": "Buddy"
}

print(pet_details)

pet_details["age"] = str(3)

print(pet_details)