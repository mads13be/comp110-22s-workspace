"""One Shot Wordle Practice."""

__author__ = "730390704"

secret_word: str = "python"
length_of_secret = len(secret_word)
user_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

while len(user_guess) != length_of_secret:
    user_guess = input(f"That was not {len(secret_word)} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

counter_variable: int = 0 
base_emoji: str = ""

while counter_variable < length_of_secret:
    if user_guess[counter_variable] == secret_word[counter_variable]:
        base_emoji = base_emoji + GREEN_BOX 
    else:
        checked_letter: bool = False
        index_of_letter: int = 0
        while index_of_letter < length_of_secret:
            if secret_word[index_of_letter] == user_guess[counter_variable]: 
                checked_letter = True
            index_of_letter = index_of_letter + 1
        if checked_letter: 
            base_emoji = base_emoji + YELLOW_BOX
        else:
            base_emoji = base_emoji + WHITE_BOX
    counter_variable = counter_variable + 1
print(base_emoji)

if user_guess == secret_word:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!") 