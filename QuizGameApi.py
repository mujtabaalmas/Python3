import requests
import html

DataofQuiz = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")
length =  len(DataofQuiz.json()["results"])
user_score = 0

if DataofQuiz.status_code == 200:
    for i in range(length):
        print(i+1 ,end=") ")
        print(html.unescape(DataofQuiz.json()["results"][i]["question"]))
        user_input = input("True or False? ").capitalize()
        if user_input ==  DataofQuiz.json()["results"][i]["correct_answer"]:
            print("Correct Answer\n")
            user_score+=1
        else:
            print("Wrong Answer\n")
    print(f"You Scored {user_score} out of {length} Questions")
else:
    print("Error occured Accesing Quiz Api !!!")
    print("Status-Code ",DataofQuiz.status_code)