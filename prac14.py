'''
Create a dictionary named student_info.
This dictionary should store the following key-value pairs:
A key "name" with a value of a student's name (e.g., "Alex").
A key "age" with a value of the student's age (e.g., 20).
A key "major" with a value of the student's major (e.g., "Computer Science").
Print the student's name by accessing the value associated with the "name" key in your student_info dictionary.
Print the student's major by accessing the value associated with the "major" key.
'''

age = int(input("What is your age?: "))
student_response = input("Are you a student? (yes/no): ")

if age < 18 and student_response == "yes":
    print("You qualify for the youth and student discount!")
else:
    print("You do not qualify for this specific discount.")