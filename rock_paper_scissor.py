import random

choices = ["rock","paper","scissor"]

user_score = 0
system_score = 0

def mainfunc(system_move,user_move):
    global user_score, system_score
    
    if system_move == "rock" and user_move == "rock":
        print(f"System move: {system_move} ---- User move: {user_move}")
    elif system_move == "paper" and user_move == "paper":
        print(f"System move: {system_move} ---- User move: {user_move}") 
    elif system_move == "scissor" and user_move == "scissor":
        print(f"System move: {system_move} ---- User move: {user_move}")

    elif system_move == "rock" and user_move == "scissor":
        print(f"System move: {system_move} ---- User move: {user_move}")
        system_score+=1
        print(f"user score: {user_score} | system score: {system_score}")

    elif system_move == "paper" and user_move == "rock":
        print(f"System move: {system_move} ---- User move: {user_move}")
        system_score+=1
        print(f"user score: {user_score} | system score: {system_score}")
        
    elif system_move == "scissor" and user_move == "paper":
        print(f"System move: {system_move} ---- User move: {user_move}")
        system_score+=1
        print(f"user score: {user_score} | system score: {system_score}")
        
    elif system_move == "rock" and user_move == "paper":
        print(f"System move: {system_move} ---- User move: {user_move}")
        user_score+=1
        print(f"user score: {user_score} | system score: {system_score}")
        
    elif system_move == "paper" and user_move == "scissor":
        print(f"System move: {system_move} ---- User move: {user_move}")
        user_score+=1
        print(f"user score: {user_score} | system score: {system_score}")
        
    elif system_move == "scissor" and user_move == "rock":
        print(f"System move: {system_move} ---- User move: {user_move}")
        user_score+=1
        print(f"user score: {user_score} | system score: {system_score}")
    
    return user_score, system_score

for i in range(3):
    system_parameter = random.choice(choices)
    user_parameter = random.choice(choices)
    print(mainfunc(system_parameter,user_parameter))

if user_score > system_score:
    print(f"User Won !!! (user score: {user_score})")
elif user_score == system_score:
    print("Draw :)")
else:
    print(f"System Won !!! (System score: {system_score})")