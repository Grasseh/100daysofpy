def guess_a_letter():
    guessed_letters = []
    guess = input("Guess a letter: ")[0].lower()
    return guess

def is_letter_in_word(word, letter):
    present = False
    for character in word:
        present = (letter == character) or present
    return present

def print_word(word, guesses):
    string = ''
    for character in word:
        if character in guesses:
            string += character
        else:
            string += '_'
        string += ' '
    print(string)

def player_won(word, guesses):
    missed_letter = False
    for character in word:
        missed_letter = missed_letter or (not character in guesses)
    return not missed_letter

def game_over(secret_word, guesses, lives):
    return player_won(secret_word, guesses) or lives == 0
