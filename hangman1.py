import random

# Predefined list of 5 words
word_list = ['apple', 'train', 'robot', 'plane', 'chair']

# Choose a random word from the list
secret_word = random.choice(word_list)

# Display version of word with underscores
display_word = ['_' for _ in secret_word]

# Track guessed letters and remaining attempts
guessed_letters = []
attempts_left = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Main game loop
while attempts_left > 0 and '_' in display_word:
    print("Word:", ' '.join(display_word))
    print("Guessed letters:", ', '.join(guessed_letters))
    print(f"Attempts left: {attempts_left}")
    
    guess = input("Enter a letter: ").lower()

    # Validate input
    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabetic character.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in secret_word:
        print("✅ Good guess!\n")
        for i, letter in enumerate(secret_word):
            if letter == guess:
                display_word[i] = guess
    else:
        print("❌ Incorrect guess.\n")
        attempts_left -= 1

# Game result
if '_' not in display_word:
    print(f"🎉 Congratulations! You guessed the word: {secret_word}")
else:
    print(f"💀 Game Over! The word was: {secret_word}")
