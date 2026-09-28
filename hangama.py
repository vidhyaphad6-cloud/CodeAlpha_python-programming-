import random


words = [
    "python",
    "computer",
    "college",
    "programming",
    "internet"
]

secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("================================")
print("        HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 wrong guesses.")

while wrong_guesses < max_wrong:

    # Display the current word
    display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong)

    
    if all(letter in guessed_letters for letter in secret_word):
        print("\n🎉 Congratulations! You guessed the word.")
        print("The word was:", secret_word)
        break

    guess = input("Enter one letter: ").lower().strip()

    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    
    if guess in secret_word:
        print("✅ Correct guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")

else:
    print("\n😢 Game Over!")
    print("The correct word was:", secret_word)

print("\nThank you for playing!")