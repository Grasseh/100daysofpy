#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
letter_len = len(letters)
number_len = len(numbers)
symbol_len = len(symbols)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for i in range(0, nr_letters):
    password += letters[random.randint(0, letter_len - 1)]
for i in range(0, nr_symbols):
    password += symbols[random.randint(0, symbol_len - 1)]
for i in range(0, nr_numbers):
    password += numbers[random.randint(0, number_len - 1)]

print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""
character_list = []
for i in range(0, nr_letters):
    character_list.append(letters)
for i in range(0, nr_symbols):
    character_list.append(symbols)
for i in range(0, nr_numbers):
    character_list.append(numbers)

random.shuffle(character_list)
for character_to_pick in character_list:
    list_len = len(character_to_pick)
    password += character_to_pick[random.randint(0, list_len - 1)]

print(password)
