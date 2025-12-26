import random
from random import choice

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
game_image=[rock,paper,scissors]

user_input=int(input("0 for rock,1 for paper,2 for scissors\n"))
print(game_image[user_input])
computer_choice=random.randint(0,2)
print(game_image[computer_choice])
if user_input>2:
    print("invalid input,you lose")
elif computer_choice==user_input:
    print("Match draw")
elif user_input==0 and computer_choice==1:
    print("You lose")
elif user_input==1 and computer_choice==2:
    print("you lose")
elif user_input==2 and computer_choice==1:
    print("you lose")
else:
    print("YOU WIn")

