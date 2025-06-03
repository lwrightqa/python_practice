"""
Ask the user to enter a sentence using the prompt: "Please enter a sentence: ".
Use a string method to split the sentence into a list of individual words. (Assume words are separated by single spaces).
Calculate how many words are in the sentence.
Print a message like: "Your sentence contains X words." where X is the number of words.
"""

sentence = input("Please enter a sentence: ")
word_list = sentence.split()
word_count = len(word_list)
print(f"Your sentence contains {word_count} words.")