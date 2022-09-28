# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
nato_alphabet = { row.letter: row.code for (i, row) in pandas.read_csv('nato_phonetic_alphabet.csv').iterrows() }

user_word = input("Enter a word to convert to Nato!")
nato_word = ' '.join([nato_alphabet[letter.upper()] for letter in user_word])
print("Here is your Nato word!")
print(nato_word)

