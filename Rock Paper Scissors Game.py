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
action = [rock, paper, scissors]

n=int(input("Enter the No. of trials : "))
i=1
player_score=0
cp_score=0
while i<=n:
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
    while player_choice > 2 or player_choice < 0:
        player_choice = int(input("enter valid input: "))
    print(action[player_choice])
        
    computer_choice = random.randint(0,2)
    print("Computer choosen: ")
    print(action[computer_choice])
        
        
    if player_choice == 0 and computer_choice == 2:
        player_score=player_score+1
        print("YOU WON!")
    elif computer_choice == 0 and player_choice == 2:
        cp_score=cp_score+1
        print("YOU LOSE!")
    elif player_choice > computer_choice:
        player_score=player_score+1
        print("YOU WON!")
    elif computer_choice > player_choice:
        cp_score=cp_score+1
        print("YOU LOSE!")
    elif player_choice == computer_choice:
        print("It's a draw")
    i=i+1

if(player_score>cp_score):
    print(f"Congratulations you won with score: {player_score-cp_score}")
elif(cp_score>player_score):
    print(f"Sorry you lost with score: {cp_score-player_score}")
else:
    print("Ohh! Game Draw")    
#Created by Akshay Tyagi