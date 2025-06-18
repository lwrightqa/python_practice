import random
import csv
import os

csv_file_path = "roster.csv"

def clear_screen():
    """Clears the terminal screen."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def get_from_roster(csv_file_path):
    try:
        with open(csv_file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader) # Skip the header
            all_players = list(reader)
            if not all_players:
                return None # No data
            return random.choice(all_players)
    except FileNotFoundError:
        print(f"Error: Name list not found.")
        return None
    except StopIteration: # Handles empty file after header
        return None

random_player = get_from_roster(csv_file_path)

position_mapping = {
    "SP1": "Starting Pitcher",
    "SP2": "Starting Pitcher",
    "SP3": "Starting Pitcher",
    "SP4": "Starting Pitcher",
    "SP5": "Starting Pitcher",
    "RP": "Relief Pitcher",
    "C": "Catcher",
    "1B": "First Baseman",
    "2B": "Second Baseman",
    "3B": "Third Baseman",
    "SS": "Shortstop",
    "LF": "Left Fielder",
    "CF": "Center Fielder",
    "RF": "Right Fielder",
    "DH": "Designated Hitter",
    "Bench (1B)": "Reserve First Baseman",
    "Bench (2B)": "Reserve Second Baseman",
    "Bench (3B)": "Reserve Third Baseman",
    "Bench (C)" : "Reserve Catcher",
    "Bench (SS)": "Reserve Shortstop",
    "Bench (LF)": "Reserve Left Fielder",
    "Bench (CF)": "Reserve Center Fielder",
    "Bench (RF)": "Reserve Right Fielder",
    "Bench (DH)": "Reserve Designated Hitter",
}

while True:
    clear_screen()
    random_player = get_from_roster(csv_file_path)

    if random_player:
        team = random_player[0]
        position_abbreviation = random_player[1]
        full_name = random_player[2]

        position_full_name = position_mapping.get(position_abbreviation, position_abbreviation)

        print(f"\n---------- Your Player is ----------")
        print(f"{full_name}, {position_full_name} for {team}.")
    else:
        print("Could not select a player. Try again.")

    if input("Get a new player? Y/N: ").lower() != "y":
        break