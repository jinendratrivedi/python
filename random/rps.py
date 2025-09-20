import random

choices = ["rock", "paper", "scissor"]

user_score = 0
computer_score = 0
rounds = 10

for i in range(rounds):
    print(f"\nRound {i + 1}:")
    user_input = input("Enter your choice (rock, paper, scissor): ").lower()
    computer_choice = random.choice(choices)

    print(f"You chose: {user_input}")
    print(f"Computer chose: {computer_choice}")

    if user_input == computer_choice:
        print("The match is a draw.")
    elif (user_input == "rock" and computer_choice == "scissor") or (user_input == "paper" and computer_choice == "rock") or (user_input == "scissor" and computer_choice == "paper"):

        print("You win this round!")
        user_score += 1
    elif user_input in choices:
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("Invalid input! Please choose rock, paper, or scissor.")

    print(f"Score => You: {user_score} | Computer: {computer_score}")

if user_score  > computer_score:
    print("user win the match")
elif computer_score > user_score:
    print("computer win the match")        
else:
    print("this match is  draw...")        