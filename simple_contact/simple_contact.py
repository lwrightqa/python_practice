# Dictionary
contact_list = []

# Menu
def display_menu():
    print("\n--- Main Menu ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

# Functions

# Add contact
def add_contact():
    contact_name = input("Name: ")
    phone_number = input("Phone Number: ")
    contact_list.append({"contact_name": contact_name, "phone_number": phone_number})
    print(f"Contact '{contact_name}' has been added successfully!")

# View all contacts
def view_all_contacts():
    if not contact_list:
        print("Your contact list is empty!")
    else:
        print("\n --- Your Contacts ---")
        # Start counting list at 1.
        for index, contact in enumerate(contact_list, start=1):
            print(f"{index}. Name: {contact['contact_name']}, Phone Number: {contact['phone_number']}")

# Search contact
def search_contact():
    if not contact_list:
        print("Your contact list is empty, so there's nothing to search.")
        return

    search_term = input("Enter the name of the contact you'd like to find.: ")
    search_term_lower = search_term.lower()
    found_contacts = []
    for contact in contact_list:
        if contact.get("contact_name", "").lower() == search_term_lower:
            found_contacts.append(contact)

    if found_contacts:
        print("\n---Found Contacts ---")
        for i, contact in enumerate(found_contacts, start=1):
            print(f"{i}. Name: {contact['contact_name']}, Phone Number: {contact['phone_number']}")
    else:
        print("No contacts found with the name " + search_term + ".")

# Delete contact
def delete_contact():
    if not contact_list:
        print("Your contact list is empty. Nothing to delete.")
        return
    view_all_contacts()
    try:
        contact_number_str = input("Enter the number of the contact to delete: ")
        contact_number_to_delete = int(contact_number_str)
        if 1 <= contact_number_to_delete <= len(contact_list):
            removed_contact = contact_list.pop(contact_number_to_delete - 1)
            print(f"Contact '{removed_contact['contact_name']}' has been deleted.")
        else:
            print("Invalid contact number. Please enter a number from the displayed list.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except IndexError:
        print("Invalid contact number.")


# Main function
def main():
    while True: # Loop to show the menu until user exits
        display_menu()
        choice_str = input("Please enter your choice 1-5: ")
        try:
            choice_int = int(choice_str) # Convert string input to integer
            if choice_int == 1: # Add contact
                add_contact()
            elif choice_int == 2:
                view_all_contacts()
            elif choice_int == 3:
                search_contact()
            elif choice_int == 4:
                delete_contact()
            elif choice_int == 5: # Exit
                print("Exiting. Goodbye!")
                break
            else:
                # Error for invalid options
                print("Invalid choice. Please enter a number between 1 and 5.")

        except ValueError: # when input cannot be converted to integer
            print(f"Invalid input: {choice_str}. Please enter a number between 1 and 5 and try again.")

        except Exception as e: # catching any other unexpected entry errors.
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()