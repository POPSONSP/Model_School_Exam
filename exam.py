"""
PROJECT:
    Write a cbt exam programme for a school whereby the 2 students will be requested to sit for an exam,
    respond to 5 random questions and at the end of the exams the score and the student name will be printed
    then the student with the maximum score will be printed.
"""
import time
nt=0
database={}
# scoreboard={}
for student in range(2):
    score=0
    user= input("Kindly input your name: ")
    # database.append(user)
    questions=["1. Where is Sqi situated ?", "2.Who is the founder of twitter ?", "3.What is the full meaning of ECOWAS ?", "4.SQI is what type of School ?", "5. Who is the president of Nigeria ?"]
    options= ["a. ABUJA \n b.KANO \n c. LAGOS \n d. IBADAN", "a. Anthony Taylor \n b.Mark Zugerberg \n c.Mike Oliver \n d. Elon Musk", 
          "a.ECONOMIC COMMUNITY OF WEST AFRICA STATES  /n b. ECONOMIC COMMON WEALTH AND STATES \n c. ECONOMIC Uninion of west African state \n d. Economic State of West Africa State.","a.Buisness \n b. Marketing \n c. Coding \n d.Agency", "a. Olusegun Obasanjo \n b. Oluyemi Osinbanjo \n C. Muhammed Buhari \n d.Bola Hammed Tinubu"]
    answers= ["d", "b", "a", "c", "c"]
    for p in range(5):
        ans= answers[p]
        print(questions[p])
        time.sleep(1)
        print(options[p])
        user_answer = input("Enter your most prefered answer: ").lower()
        if user_answer == answers[p]:
           print("Correct")
           score += 10
        else:
           print("Wrong")
        print(f"Congrats, Your exam is over and your total score is {score}") 
    database.update({user:score})
print(database)   
max_value= max(database.items())   
max_value_key=max(database,key=database.get)       
print(max_value) 
print("the student that has the maximum score is: ", max_value_key)

