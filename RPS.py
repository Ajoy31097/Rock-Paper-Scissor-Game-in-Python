import random
import time

print("Welcome to Rock-Paper-Scissors Game")

user_score = 0
comp_score = 0
ties = 0

name = input("Enter your name: ")

print()

print("Hello", name)

print("""

Rules of the Game:
    1. Paper vs Rock --> Paper
    2. Paper vs Scissors --> Scissors
    3. Scissors vs Rock --> Rock
""")

while True:

    print("""
    Choices are:
        1. Rock
        2. Paper
        3. Scissors
    """)

    choice = int(input("Enter your choice from 1 to 3: "))

    print()

    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input"))

    if choice == 1:
        user_choice = "Rock"

    elif choice == 2:
        user_choice = "Paper"

    else:
        user_choice = "Scissors"


    print("You have played:", user_choice)
    print()
    print("Now its computer's turn...")
    print()

    time.sleep(3)
    computer = random.randint(1,3)

    if computer == 1:
        comp_choice = "Rock"

    elif computer == 2:
        comp_choice = "Paper"

    else:
        comp_choice = "Scissors"

    print("Computer has played:", comp_choice)
    print()

    if((user_choice == "Paper" and comp_choice == "Rock") or (comp_choice == "Paper" and user_choice == "Rock")):
        result = "Paper"

    elif((user_choice == "Scissors" and comp_choice == "Rock") or (comp_choice == "Scissors" and user_choice == "Rock")):
        result = "Rock"

    elif(user_choice == comp_choice):
        print("Its a tie")
        result = "Tie"

    else:
        result = "Scissors"

    if result == "Tie":
        ties += 1

    elif result == user_choice:
        print(name,"Wins")
        user_score +=1

    else:
        print("Computer Wins")
        comp_score +=1


    print("\nScores:")
    print(name,":", user_score)
    print("Computer:", comp_score)
    print("Ties:", ties)
    print()

    repeat = input("Do you want to play again? (yes/no) ")  
    if repeat.lower() == "no": 
        print("Game Over!")
        print()
        print("Thank you for playing")
        break



