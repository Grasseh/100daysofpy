import random
import methods
import hangman_art
import words

print(hangman_art.logo)
word_list = words.word_list

secret_word = random.sample(word_list, 1)[0]
guesses = []
methods.print_word(secret_word, guesses)
lives = 6

while(not methods.game_over(secret_word, guesses, lives)):
    guess = methods.guess_a_letter()
    if guess in guesses:
        print(f"You already guessed {guess}")
    else:
        guesses.append(guess)

        if methods.is_letter_in_word(secret_word, guess):
            print(f"{guess} is in the word!")
        else:
            print(f"{guess} is wrong! You lose a life!")
            lives -= 1

    print(hangman_art.stages[lives])
    methods.print_word(secret_word, guesses)

if lives == 0:
    print("You lose!")
    print(f"The word you were looking for was {secret_word}")
else:
    print("You won!")
