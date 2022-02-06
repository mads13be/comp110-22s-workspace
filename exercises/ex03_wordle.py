"""Exercise Three- Wordle."""

__author__ = "730390704"


def contains_char(length_of_word: str, single_character: str) -> bool:
    """A function that results in a bool statement."""
    assert len(single_character) == 1
    i: int = 0
    while i < len(length_of_word): 
        if single_character == length_of_word[i]:
            return True
        else:
            i = i + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """A function that returns as a string."""
    assert len(guess) == len(secret)
    emoji_base: str = ""
    counter_variable: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    while counter_variable < len(secret):
        if guess[counter_variable] == secret[counter_variable]:
            emoji_base += GREEN_BOX
        else: 
            if contains_char(secret, guess[counter_variable]):
                emoji_base += YELLOW_BOX
            else:
                emoji_base += WHITE_BOX
        counter_variable += 1
    return emoji_base 


def input_guess(expected_length: int) -> str:
    """A function that returns the user's guess of the correct length."""
    guess_word: str = input("Enter a five character word")
    while len(guess_word) != expected_length:
        guess_word: str = input(f"That wasn't {expected_length} chars! Try again")
    return guess_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    length_of_secret: int = len(secret_word)
    turn: int = 1
    won: bool = False
    
    while turn < 7 and not won:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(length_of_secret)
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print("You won in {turn}/6 turns!")
            won = True
        turn += 1
        if guess != secret_word:
            print("{turn}/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()