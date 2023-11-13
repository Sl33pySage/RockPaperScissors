import random
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


print("Welcome to Rock Paper Scissors!")
choice = int(input("Please type '0' for 'Rock', '1' for 'Paper', and '2' for 'Scissors':\n"))

if choice == 0:
  print("You've chosen Rock!")
  print(rock)
  
elif choice == 1:
  print("You've chosen Paper!")
  print(paper)

elif choice == 2:
  print("You've chosen Scissors!")
  print(scissors)
  
computer_choice = random.randint(0,2)

if choice >= 3 or choice < 0:
  print("Invalid choice! YOU LOSE!")

elif computer_choice == 0:
  print("The Computer has chosen Rock!")
  print(rock)

elif computer_choice == 1:
  print("The Computer has chosen Paper!")
  print(paper)

else:
  print("The Computer has chosen Scissors!")
  print(scissors)

if choice == computer_choice:
  print("DRAW!")

elif (choice == 0) and (computer_choice == 1):
  print("Paper covers Rock! YOU LOSE!")

elif (choice == 1) and (computer_choice == 0):
  print("Paper covers Rock! YOU WIN!")

elif (choice == 2) and (computer_choice == 1):
  print("Scissors cuts Paper! YOU WIN!")

elif (choice == 1) and (computer_choice == 2):
  print("Scissors cuts Paper! YOU LOSE!")

elif (choice == 2) and (computer_choice == 0):
  print("Rock crushes Scissors! YOU LOSE!")

elif (choice == 0) and (computer_choice == 2):
  print("Rock crushes Scissors! YOU WIN!")