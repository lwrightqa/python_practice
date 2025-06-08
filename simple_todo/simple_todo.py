"""
1.Display a Menu:•When the program starts, and after each action, display a menu of options to the user.
2.Add Task:
•If the user chooses "Add task", prompt them to enter the task description.
•Store this task in a Python list.
•Confirm to the user that the task has been added.
3.View task_list:
If the user chooses "View task_list":
•If the list is empty, print a message like "Your to-do list is empty!"
•Otherwise, display all the task_list currently in the list. For a better user experience, number the task_list when displaying
them.
4.Mark Task as Complete (Remove Task):
•If the user chooses "Mark task as complete":
•If the list is empty, inform them and do nothing further for this option.
•Display the task_list with numbers (similar to "View task_list").
•Ask the user to enter the number of the task they want to remove.
•Validate the input:•Ensure it's a valid number.
•Ensure the number corresponds to an actual task in the list.
•If valid, remove the specified task from the list and confirm its removal.
•If invalid (e.g., number out of range, non-numeric input), show an appropriate error message.
5.Exit: If the user chooses "Exit", print a goodbye message and terminate the program.
6.Loop: The program should continue to display the menu and accept user input until the user explicitly chooses to "Exit".
"""

# Task list to store task_list
task_list = ["Add your first task to the list"]

# Functions
def display_menu():
    # Prints menu options to the console
    print("\n--- Main Menu ---")
    print("1. Add Task")
    print("2. View Task List")
    print("3. Complete/Remove Task")
    print("4. Exit")
    print("-----------------")

# Defining add new task
def add_new_task():
    task = input("Enter the task description: ")
    task_list.append(task)
    print(f"Task '{task}' has been added successfully!")

# Defining view task list
def view_task_list():
    if not task_list:
        print("Your to-do list is empty!")
    else:
        print("\n --- Your Tasks ---")
        # Start counting list at 1.
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")
        print("-----------------")

# Defining complete/remove task
def complete_task():
    if not task_list: # If task list is empty
        print("You have no tasks to complete.")
        return
    view_task_list()

    try:
        task_number_str = input("Enter the number of the task to complete and remove it from the list: ")
        task_number_to_remove = int(task_number_str)

        if 1 <= task_number_to_remove <= len(task_list):
            # Remove the task from the list and return it
            removed_task = task_list.pop(task_number_to_remove - 1)
            print(f"Task '{removed_task}' marked complete and removed.")
        else:
            print("Invalid task number. Please enter a number from the displayed list.")
    except ValueError:
        # When input is not a number
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        # Other unexpected entry errors
        print(f"An unexpected error occurred while trying to remove a task: {e}")


# Main function
def main():
    while True: # Loop to show the menu until user exits
        display_menu()
        choice_str = input("Please enter your choice 1-4: ")
        try:
            choice_int = int(choice_str) # Convert string input to integer
            if choice_int == 1: # Add task
                print("You selected Add Task")
                add_new_task()
            elif choice_int == 2:
                print("You selected View Task List")
                view_task_list()
            elif choice_int == 3:
                print("You selected Complete/Remove Task")
                complete_task()
            elif choice_int == 4: # Exit
                print("Exiting. Goodbye!")
                break
            else:
                # Error for invalid options
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError: # when input cannot be converted to integer
            print(f"Invalid input: {choice_str}. Please enter a number between 1 and 4 and try again.")
        except Exception as e: # catching any other unexpected entry errors.
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()