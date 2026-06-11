import random

# List of 5 predefined words
words = ["apple", "train", "house", "tiger", "chair"]

# Select a random word
word = random.choice(words)

# Create hidden word display
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
incorrect_guesses = 0
max_incorrect = 6

print("=== Hangman Game ===")

while incorrect_guesses < max_incorrect and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Check for valid input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is in word
    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

# Game result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
