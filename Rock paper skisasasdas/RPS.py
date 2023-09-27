import random

user_wins = 0
comp_wins = 0
draws = 0

options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Coputer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You win")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You win")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You win")
        user_wins += 1

    elif user_input == computer_pick:
        print("Draw")
        draws += 1

    else:
        print("You lost")
        comp_wins += 1


print("Your won:", user_wins, "Computer wins:", comp_wins, "Draws:", draws)
print("Done")
