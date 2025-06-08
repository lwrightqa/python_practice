"""
Create an empty list named my_tasks.
Print a message that says "Initial number of tasks: " followed by the number of items currently in my_tasks. (Hint: The len() function can tell you the length of a list).
Add the following three tasks (as strings) to the my_tasks list, one at a time, using the list's .append() method:
"walk the dog"
"buy groceries"
"read a chapter"
After adding all three tasks, print a message that says "Updated number of tasks: " followed by the new number of items in my_tasks.
Finally, print the entire my_tasks list to the console.
"""

my_tasks = []
print(f"Initial number of tasks: {len(my_tasks)}")

my_tasks.append("walk the dog")
my_tasks.append("buy groceries")
my_tasks.append("read a chapter")

print(f"Updated number of tasks: {len(my_tasks)}")

print(my_tasks)