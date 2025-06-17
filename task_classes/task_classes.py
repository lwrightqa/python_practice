# This is a Python application to manage tasks using Object-Oriented Programming (OOP) concepts.
# We will define two classes: 'Task' and 'TaskManager'.

class Task:
    """
    Represents a single task with its description, status (completed or not), and an optional due date.
    This is our blueprint for individual task objects.
    """

    # The __init__ method is a special method called a constructor.
    # It's automatically invoked when you create a new instance (object) of the Task class.
    # 'self' refers to the instance of the class being created or operated upon.
    # 'description', 'due_date', and 'completed' are parameters passed when creating a Task object.
    def __init__(self, description, due_date=None, completed=False):
        """
        Initializes a new Task object.

        Args:
            description (str): A brief summary of the task.
            due_date (str, optional): The due date of the task (e.g., "2025-12-31"). Defaults to None.
            completed (bool, optional): The completion status of the task. Defaults to False.
        """
        # Assigning the 'description' parameter to an instance variable called 'self.description'.
        # This makes 'description' an attribute of the Task object.
        self.description = description
        # Assigning the 'due_date' parameter to an instance variable 'self.due_date'.
        self.due_date = due_date
        # Assigning the 'completed' parameter to an instance variable 'self.completed'.
        # This attribute will track if the task is done.
        self.completed = completed

    def mark_as_completed(self):
        """
        Marks the task as completed.
        This is a method (a function defined within a class) that modifies an attribute of the object.
        'self' allows us to access and modify the 'completed' attribute of the specific Task object.
        """
        self.completed = True
        # Print a confirmation message indicating which task has been marked.
        print(f"Task '{self.description}' marked as completed.")

    def get_status(self):
        """
        Returns the current status of the task as a string.
        This is a method that provides information about the object's state (its 'completed' attribute).
        """
        # Use a ternary operator for concise status output: "Completed" if True, "Pending" if False.
        return "Completed" if self.completed else "Pending"

    def get_details(self):
        """
        Returns a formatted string containing all details of the task.
        This method combines attributes to present a full view of the task object.
        """
        # Get the status string using the get_status() method of this same Task object.
        status_str = self.get_status()
        # Check if a due date exists to include it in the details.
        if self.due_date:
            # Format the output string using f-strings for readability.
            return f"Description: '{self.description}', Due: {self.due_date}, Status: {status_str}"
        else:
            # Return details without a due date if it's not set.
            return f"Description: '{self.description}', Status: {status_str}"

class TaskManager:
    """
    Manages a collection of Task objects.
    This class will serve as a container and controller for all our Task instances.
    It demonstrates how one class can contain and operate on objects of another class (composition).
    """

    def __init__(self):
        """
        Initializes a new TaskManager object.
        The constructor for TaskManager sets up an empty list to hold Task objects.
        """
        # 'self.tasks' is an attribute of the TaskManager object.
        # It's an empty list that will store all the 'Task' instances we create.
        self.tasks = []

    def add_task(self, description, due_date=None):
        """
        Creates a new Task object and adds it to the manager's list of tasks.

        Args:
            description (str): The description for the new task.
            due_date (str, optional): The due date for the new task. Defaults to None.
        """
        # Create a new instance (object) of the 'Task' class.
        # This is where we use the Task blueprint to create an actual task.
        new_task = Task(description, due_date)
        # Append the newly created 'new_task' object to the 'self.tasks' list.
        self.tasks.append(new_task)
        # Print a confirmation message.
        print(f"Task '{description}' added.")

    def list_tasks(self):
        """
        Lists all tasks currently managed by the TaskManager.
        It iterates through the 'self.tasks' list and prints details of each Task object.
        """
        # Check if the 'tasks' list is empty.
        if not self.tasks:
            print("No tasks in the list.")
            # If empty, exit the method.
            return

        print("\n--- Your Tasks ---")
        # Loop through each task object in the 'self.tasks' list.
        # 'enumerate' provides both the index (i) and the task object itself.
        for i, task in enumerate(self.tasks):
            # Print the task number (i + 1 for 1-based indexing) and its details.
            # We call the 'get_details()' method on each individual 'task' object.
            print(f"{i + 1}. {task.get_details()}")
        print("------------------")

    def mark_task_complete(self, task_number):
        """
        Marks a specific task as completed based on its number in the list.

        Args:
            task_number (int): The 1-based index of the task to mark as complete.
        """
        # Adjust 'task_number' to be 0-based index for list access.
        actual_index = task_number - 1
        # Check if the provided index is valid (within the bounds of the list).
        if 0 <= actual_index < len(self.tasks):
            # Get the specific Task object from the list using its index.
            task_to_complete = self.tasks[actual_index]
            # Call the 'mark_as_completed()' method on that specific Task object.
            task_to_complete.mark_as_completed()
        else:
            # Inform the user if the task number is invalid.
            print("Invalid task number.")

    def delete_task(self, task_number):
        """
        Deletes a task from the list based on its number.

        Args:
            task_number (int): The 1-based index of the task to delete.
        """
        # Adjust 'task_number' to be 0-based index for list access.
        actual_index = task_number - 1
        # Check if the provided index is valid.
        if 0 <= actual_index < len(self.tasks):
            # Remove the task object from the list using its index.
            # The 'pop' method removes and returns the item at the given index.
            removed_task = self.tasks.pop(actual_index)
            # Print a confirmation message, showing the description of the removed task.
            print(f"Task '{removed_task.description}' deleted.")
        else:
            # Inform the user if the task number is invalid.
            print("Invalid task number.")

def display_menu():
    """
    Displays the interactive menu options to the user.
    This is a regular function, not part of a class, as it's a utility for the main program flow.
    """
    print("\n--- Task Management Menu ---")
    print("1. Add a new task")
    print("2. List all tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Exit")
    print("----------------------------")

def get_integer_input(prompt):
    """
    Helper function to get integer input from the user with error handling.

    Args:
        prompt (str): The message to display to the user.

    Returns:
        int: The valid integer input.
    """
    while True:
        try:
            # Try to convert the user's input to an integer.
            value = int(input(prompt))
            # If successful, return the value.
            return value
        except ValueError:
            # If conversion fails (e.g., user types text), print an error.
            print("Invalid input. Please enter a number.")

def main():
    """
    The main function that runs the Task Management application.
    This function orchestrates the interaction between the user and the TaskManager.
    """
    # Create an instance (object) of the TaskManager class.
    # This 'my_manager' object will hold and manage all our tasks.
    my_manager = TaskManager()

    # Start an infinite loop to keep the application running until the user chooses to exit.
    while True:
        # Display the menu options to the user.
        display_menu()
        # Get the user's choice as a string.
        choice = input("Enter your choice (1-5): ")

        # Use if/elif/else to handle different user choices.
        if choice == '1':
            # If choice is '1', prompt for task details.
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional, e.g., YYYY-MM-DD), press Enter if none: ")
            # If the user didn't enter a due date, set it to None.
            if not due_date:
                due_date = None
            # Call the 'add_task' method on our 'my_manager' object.
            # This method will create a new Task object internally.
            my_manager.add_task(description, due_date)
        elif choice == '2':
            # If choice is '2', call the 'list_tasks' method to display all tasks.
            my_manager.list_tasks()
        elif choice == '3':
            # If choice is '3', ask the user which task to mark as complete.
            # Use our helper function to ensure integer input.
            task_num = get_integer_input("Enter the number of the task to mark as complete: ")
            # Call the 'mark_task_complete' method on our 'my_manager' object.
            my_manager.mark_task_complete(task_num)
        elif choice == '4':
            # If choice is '4', ask the user which task to delete.
            # Use our helper function to ensure integer input.
            task_num = get_integer_input("Enter the number of the task to delete: ")
            # Call the 'delete_task' method on our 'my_manager' object.
            my_manager.delete_task(task_num)
        elif choice == '5':
            # If choice is '5', print an exit message and break out of the while loop.
            print("Exiting Task Management application. Goodbye!")
            break # This statement terminates the 'while True' loop.
        else:
            # If the choice is anything else, it's an invalid input.
            print("Invalid choice. Please enter a number between 1 and 5.")

# This is a common Python idiom.
# It ensures that the 'main()' function is called only when the script is executed directly
# (not when it's imported as a module into another script).
if __name__ == "__main__":
    main() # Call the main function to start the application.