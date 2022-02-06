"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730390704"

character_word: str = input("Enter a 5-character word: ")
if 5 != len(character_word):
    print("Error: Word must contain 5 characters ")
    exit()
letter: str = input("Enter a single character: ")
if 1 != len(letter):
    print("Error: Character must be a single character. ")
    exit()
print("Searching for " + letter + " in " + character_word)
instances: int = 0

if character_word[0] == letter:
    print(letter + " found at index 0 ")
    instances = instances + 1
if character_word[1] == letter:
    print(letter + " found at index 1 ")
    instances = instances + 1
if character_word[2] == letter:
    print(letter + " found at index 2 ")
    instances = instances + 1
if character_word[3] == letter:
    print(letter + " found at index 3 ")
    instances = instances + 1
if character_word[4] == letter:
    print(letter + " found at index 4 ") 
    instances = instances + 1 

if instances == 0:
    print("No instances of " + letter + " found in " + character_word)
elif instances == 1:
    print("1 instance of " + letter + " found in " + character_word)
else:
    instances_occured = str(instances)
    print(instances_occured + " instances of " + letter + " found in " + character_word) 