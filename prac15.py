'''
Ask the user to enter their age. Convert this input to an integer.
Ask the user if they are a student. The prompt should be "Are you a student? (yes/no): ". Store their response (it will be a string like "yes" or "no").
Use an if-else statement with a compound condition (using and):
If the user's age is less than 18 and their response to being a student is exactly "yes", then print: "You qualify for the youth and student discount!"
Otherwise (if the condition above is not met), print: "You do not qualify for this specific discount."
'''

age = int(input("What is your age?: "))
student_response = input("Are you a student? (yes/no): ")

if age < 18 and student_response == "yes":
    print("You qualify for the youth and student discount!")
else:
    print("You do not qualify for this specific discount.")