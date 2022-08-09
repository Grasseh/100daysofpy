rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choice = int(input('Choose 0 for rock, 1 for paper and 2 for scissors'))

symbol_list = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
difference = (computer_choice - choice) % 3
if difference == 2:
    result = "You win!"
elif difference == 1:
    result = "You lose!"
else:
    result = "It's a draw!"

print("You chose:")
print(symbol_list[choice])
print("The computer chose:")
print(symbol_list[computer_choice])
print(result)
