import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_move = input("Type Rock/Paper/Scissors or L to leave.")
    if user_move == "L":
        break
    if user_move in options:
        random_number = random.randint(0,2)
        #rock: 0, paper: 1, scissors: 2
        computer_move = options[random_number]
        print(f"The Computer picked {computer_move}")
        if user_move == "rock" and computer_move == "scissors":
            print("You won!")
            user_wins += 1
        elif user_move == "paper" and computer_move == "rock":
            print("You won!")
            user_wins += 1
        elif user_move == "scissors" and computer_move == "paper":
            print("You won!")
            user_wins += 1
        elif user_move == computer_move:
            print("Its a tie!")
        else:
            print("You lost!")
            computer_wins += 1
    else:
        print("Invalid Value Try again.")

print("Thank you for playing :)")
print(f"You have won {user_wins} times, the computer has won {computer_wins} times.")