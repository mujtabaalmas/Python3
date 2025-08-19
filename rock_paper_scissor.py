import random

choices = ("rock","paper","scissor")

user_score = 0
system_score = 0

def mainfunc(system_move,user_move):
    global user_score, system_score
    
    if system_move == "rock" and user_move == "rock":
        print(f"System move: {system_move}  User move: {user_move}")
    elif system_move == "paper" and user_move == "paper":
        print(f"System move: {system_move}  User move: {user_move}") 
    elif system_move == "scissor" and user_move == "scissor":
        print(f"System move: {system_move}  User move: {user_move}")

    elif system_move == "rock" and user_move == "scissor":
        print(f"System move: {system_move}  User move: {user_move}")
        system_score+=1
        print(f"user score: {user_score} | system score: {system_score}")

    elif system_move == "paper" and user_move == "rock":
        print(f"System move: {system_move}  User move: {user_move}")
        system_score+=1
        print(f"user score: {user_score} | system score: {system_score}")
        
    elif system_move == "scissor" and user_move == "paper":
        print(f"System move: {system_move}  User move: {user_move}")
        system_score+=1
        print(f"user score: {user_score} | system score: {system_score}")
        
    elif system_move == "rock" and user_move == "paper":
        print(f"System move: {system_move}  User move: {user_move}")
        user_score+=1
        print(f"user score: {user_score} | system score: {system_score}")
        
    elif system_move == "paper" and user_move == "scissor":
        print(f"System move: {system_move}  User move: {user_move}")
        user_score+=1
        print(f"user score: {user_score} | system score: {system_score}")
        
    elif system_move == "scissor" and user_move == "rock":
        print(f"System move: {system_move}  User move: {user_move}")
        user_score+=1
        print(f"user score: {user_score} | system score: {system_score}")
    
    return user_score, system_score

def runfunc(mainfunc):
    round_count = int(input("How many rounds you want to play: "))
    if round_count < 1:
        print(f"Invalid Round choice {round_count}")
    elif round_count > 5:
        print("Cannot play more than 5 rounds ")
    else:
        for i in range(round_count):
            print()
            system_parameter = random.choice(choices)
            user_parameter = input('Enter your choice to defeat system i.e "rock" "paper" "scissor": ').lower()
            if user_parameter not in choices:
                print(f"Error: {user_parameter} Invalid choice please try again")
            print(mainfunc(system_parameter,user_parameter))

        if user_score > system_score:
            print(f"\nUser Won !!! (user score: {user_score})")
        elif user_score == system_score:
            print("\nDraw :)")
        else:
            print(f"\nSystem Won !!! (System score: {system_score})")



runfunc(mainfunc)