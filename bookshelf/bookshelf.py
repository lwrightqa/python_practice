import json  # For JSON operations
import os  # To check if file exists


# The initial comment block describing the Book dictionary structure
# is not valid Python code and should be removed or commented out.
# For example:
# Book {
# 	'title': book.title,
# 	'author': book.author
# 	'year': book.year
# }

class Book:
	# Represents a single book with title, author and publication year.
	def __init__(self, title, author, year):
		self.title = title  # 'self.title' is an attribute
		self.author = author  # 'self.author' is an attribute
		self.year = year  # 'self.year' is an attribute

	def get_details(self):  # This is a method
		return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

	def to_dict(self):
		# Returns a dictionary representation of the book.
		return {'title': self.title, 'author': self.author, 'year': self.year}


class Library:
	# Manage collection of book objects
	def __init__(self, filepath="library_data.json"):
		# Initializing library, potentially loading from file.
		self.books = []  # List with book objects
		self.filepath = filepath
		self.load_books_from_file()

	def add_book(self, title, author, publication_year):
		# Ensure publication_year is an int before creating Book object
		try:
			year = int(publication_year)
			self.books.append(Book(title, author, year))
			print(f"Added book: '{title}' by {author}")
		except ValueError:
			print(f"Error: Publication year '{publication_year}' for '{title}' is not a valid number.")

	def list_books(self):
		# Lists all books in library.
		if not self.books:
			print("The library is empty.")
			return

		print("\n--- Current Books in Library ---")
		for i, book in enumerate(self.books):
			print(f"{i + 1}. {book.get_details()}")
		print("--------------------------------")

	def find_book(self, search_term):
		# Searches for books by title or author (case-insensitive)
		found_books = []
		search_term_lower = search_term.lower()

		for book in self.books:
			if search_term_lower in book.title.lower() or \
					search_term_lower in book.author.lower():
				found_books.append(book)

		# Moved this block outside the loop
		if not found_books:
			print(f"No books found for '{search_term}'.")
		else:
			print(f"\n--- Books matching '{search_term}' ---")
			for book in found_books:
				print(book.get_details())
			print("------------------------------------")

	# Removed: choice = input("Enter your choice (1-4): ") as it's out of place here

	def save_books_to_file(self):
		# Saves the current list of books to the JSON file.
		# Convert list of Book objects to list of dictionaries
		books_data = [book.to_dict() for book in self.books]
		try:
			with open(self.filepath, 'w') as f:
				json.dump(books_data, f, indent=4)  # indent for readability
			print(f"Library saved to {self.filepath}")
		except IOError:
			print(f"Error: Could not save library to {self.filepath}")

	def load_books_from_file(self):
		# Loads books from the JSON file.
		if not os.path.exists(self.filepath):
			print(f"Data file '{self.filepath}' not found. Starting with an empty library.")
			return  # No file to load, start fresh

		try:
			with open(self.filepath, 'r') as f:
				books_data = json.load(f)
				# Convert list of dictionaries back to list of Book objects
				for book_dict in books_data:
					# Basic validation for required keys
					if 'title' in book_dict and 'author' in book_dict and 'year' in book_dict:
						self.books.append(Book(book_dict['title'], book_dict['author'], int(book_dict['year'])))
					else:
						print(f"Warning: Skipping invalid book data: {book_dict}")
			print(f"Library loaded from {self.filepath}")
		except json.JSONDecodeError:
			print(
				f"Error: Could not decode JSON from {self.filepath}. File might be corrupted. Starting with an empty library.")
			self.books = []  # Reset to empty if file is corrupt
		except IOError:
			print(f"Error: Could not read library from {self.filepath}. Starting with an empty library.")
			self.books = []  # Reset to empty if file cannot be read
		except ValueError:  # Handles case where year in JSON is not an int
			print(f"Error: Invalid year format in {self.filepath}. Starting with an empty library.")
			self.books = []


def main():
	# Main function to run the Book Collection Manager application.
	library_file = "my_books.json"  # Define the filename for storing data
	my_library = Library(filepath=library_file)

	while True:
		print("\n--- Book Collection Manager Menu ---")
		print("1. Add a new book")
		print("2. List all books")
		print("3. Search for a book")
		print("4. Exit")
		print("------------------------------------")

		choice = input("Enter your choice (1 - 4): ")

		if choice == "1":
			title = input("Enter book title: ")
			author = input("Enter book author: ")
			while True:
				try:
					year_str = input("Enter publication year: ")
					year = int(year_str)  # Attempt conversion here
					break
				except ValueError:
					print("Invalid year. Please enter a valid number.")
			my_library.add_book(title, author, year)  # Pass the integer year
		elif choice == "2":
			my_library.list_books()
		elif choice == "3":
			search_term = input("Enter title or author to search: ")
			my_library.find_book(search_term)
		elif choice == "4":
			my_library.save_books_to_file()  # Save before exiting
			print("Exiting Book Collection Manager. Goodbye!")
			break
		else:
			print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
	main()