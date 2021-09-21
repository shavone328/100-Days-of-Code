import random

# Choice images
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

choices = ["Rock", "Paper", "Scissors"]
user_choice = input("Choose: Rock, Paper, or Scissors?")
computer_choice = choices[random.randint(0,2)]

# Outcomes 
# User chooses Rock
if user_choice == "Rock":
    print("You chose Rock:\n" + rock)
    # Case 1: Tie
    if computer_choice == "Rock":
        print("Computer chose Rock:\n" + rock)
        print("IT'S A TIE!")
    # Case 2: You lose
    elif computer_choice == "Paper":
        print("Computer chose Paper:\n" + paper)
        print("Paper beats Rock, YOU LOSE!")
    # Case 3: You win
    elif computer_choice == "Scissors":
        print("Computer chose Scissors:\n" + scissors)
        print("Rock beats Scissors, YOU WIN!")
    
    
# User chooses Paper
elif user_choice == "Paper":
    print("You chose Paper:\n" + paper)
    # Case 1: Tie
    if computer_choice == "Paper":
        print("Computer chose Paper:\n" + paper)
        print("IT'S A TIE!")
    # Case 2: You lose
    elif computer_choice == "Scissors":
        print("Computer chose Scissors:\n" + scissors)
        print("Scissors beats Paper, YOU LOSE!")
    # Case 3: You win
    elif computer_choice == "Rock":
        print("Computer chose Rock:\n" + rock)
        print("Paper beats Rock, YOU WIN!")
        
# User chooses Scissors
elif user_choice == "Scissors":
    print("You chose Scissors:\n" + scissors)
    # Case 1: Tie
    if computer_choice == "Scissors":
        print("Computer chose Scissors:\n" + scissors)
        print("IT'S A TIE!")
    # Case 2: You lose
    elif computer_choice == "Rock":
        print("Computer chose Rock:\n" + rock)
        print("Rock beats Scissors, YOU LOSE!")
    # Case 3: You win
    elif computer_choice == "Paper":
        print("Computer chose Paper:\n" + paper)
        print("Scissors beats Paper, YOU WIN!")