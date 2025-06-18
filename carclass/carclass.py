import pickle
import os

GARAGE_FILE = "garage.pkl"

class Garage:
    def __init__(self):
        self.cars = []

class Car:
    def __init__(self, color, year, make, model):
        self.color = color
        self.year = year
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.color} {self.year} {self.make} ({self.model})"

# Load garage data or initialize an empty one
if os.path.exists(GARAGE_FILE):
    try:
        with open(GARAGE_FILE, "rb") as f:
            my_garage = pickle.load(f)
        # Ensure loaded data is a Garage instance
        if not isinstance(my_garage, Garage):
            print(f"Warning: Data in {GARAGE_FILE} is not a valid Garage. Starting with an empty garage.")
            my_garage = Garage()
    except (pickle.UnpicklingError, EOFError, AttributeError) as e:
        print(f"Error loading {GARAGE_FILE}: {e}. Starting with a new empty garage.")
        my_garage = Garage()
else:
    my_garage = Garage()

while True:
    print("\n--------- GARAGE MAIN MENU ---------")
    print("1. Add Car")
    print("2. List Cars")
    print("3. Delete Car")
    print("4. Exit")
    print("------------------------------------")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Adding Car...")
        color = input("Enter color: ")
        year = input("Enter year: ")
        make = input("Enter make: ")
        model = input("Enter model: ") # Corrected variable name
        new_car = Car(color, year, make, model)
        my_garage.cars.append(new_car)
        print(f"Car '{new_car}' added to the garage.")
        try:
            with open(GARAGE_FILE, "wb") as f:
                pickle.dump(my_garage, f)
            print("Garage saved.")
        except IOError as e:
            print(f"Error saving garage to {GARAGE_FILE}: {e}")

    elif choice == "2":
        print("\nListing Cars...")
        if not my_garage.cars:
            print("The garage is empty.")
        else:
            for i, car_obj in enumerate(my_garage.cars):
                print(f"{i + 1}. {car_obj}")

    elif choice == "3":
        print("Deleting Car...")
        if not my_garage.cars:
            print("The garage is empty. Nothing to delete.")
        else:
            print("Current cars in garage:")
            for i, car_obj in enumerate(my_garage.cars):
                print(f"{i + 1}. {car_obj}")
            try:
                car_num_to_delete = int(input("Enter the number of the car to delete: "))
                if 1 <= car_num_to_delete <= len(my_garage.cars):
                    deleted_car = my_garage.cars.pop(car_num_to_delete - 1)
                    print(f"Car '{deleted_car}' deleted successfully.")
                    try:
                        with open(GARAGE_FILE, "wb") as f:
                            pickle.dump(my_garage, f)
                        print("Garage saved.")
                    except IOError as e:
                        print(f"Error saving garage to {GARAGE_FILE}: {e}")
                else:
                    print("Invalid car number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif choice == "4":
        print("Exiting and saving garage...")
        break
    else:
        print("Invalid choice. Please try again.")