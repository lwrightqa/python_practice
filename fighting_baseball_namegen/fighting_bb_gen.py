import random
import csv

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

csv_file_path = "roster.csv"
random_player = get_from_roster(csv_file_path)

if random_player:
	position_mapping = {
		"SP1": "Starting Pitcher 1",
		"SP2": "Starting Pitcher 2",
		"SP3": "Starting Pitcher 3",
		"SP4": "Starting Pitcher 4",
		"SP5": "Starting Pitcher 5",
		"RP": "Relief Pitcher",
		"C": "Catcher",
		"1B": "First Baseman",
		"2B": "Second Baseman",
		"3B": "Third Baseman",
		"SS": "Shortstop",
		"LF": "Left Fielder",
		"CF": "Center Fielder",
		"RF": "Right Fielder",
		"DH": "Designated Hitter"
	}

team = random_player[0]
position_abbreviation = random_player[1]
full_name = random_player[2]

position_full_name = position_mapping.get(position_abbreviation, position_abbreviation)

if random_player: # Checking that lists are not empty
	print(f"Your name is {full_name}.\nYour spot on the roster is {position_full_name}.\nYour team is {team}")
else:
	print("Could not select a player. Try again.")