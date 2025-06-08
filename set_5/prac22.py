"""
Create a list named guest_list and initialize it with the following names: ["Alice", "Bob", "Charlie", "David"].
Print the initial guest_list.
Ask the user to enter a name they'd like to remove from the list using the prompt: "Which guest would you like to remove? ".
Check if the entered name is actually in the guest_list.
If the name is in the list:
Remove the name from guest_list.
Print a message like: "[Name] has been removed from the guest list." (where [Name] is the actual name).
If the name is not in the list:
Print a message like: "[Name] was not found on the guest list." (where [Name] is the actual name).
Finally, print the updated guest_list (it will either be unchanged or have one name removed).
"""

guest_list = ["Alice", "Bob", "Charlie", "David"]

print("Initial list: ", guest_list)

guest_to_remove = input("Which guest would you like to remove? ")

if guest_to_remove in guest_list:
    guest_list.remove(guest_to_remove)
    print(f"{guest_to_remove} has been removed from the guest list.")
else:
    print(f"{guest_to_remove} was not found on the guest list.")

print("The current guest list includes:", guest_list)

exit()