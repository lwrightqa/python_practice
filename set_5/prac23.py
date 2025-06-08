"""
Create a dictionary named book_details with the following key-value pairs:
"title": "The Great Gatsby"
"author": "F. Scott Fitzgerald"
"year": 1925
Use a for loop to iterate through the book_details dictionary.
Inside the loop, for each key-value pair, print them in the format: "Key: Value". For example, for the first item, it should print: title: The Great Gatsby
"""
# Dictionary
book_details: dict = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
}

for key, value in book_details.items():
    print(f"{key}: {value}")

exit()