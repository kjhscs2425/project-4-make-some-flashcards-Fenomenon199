import random 
import json 
with open ("data.json", "r") as f:
    data= json.load (f)  
flashcards= {
   "How many people use an apple product in the world?" : " 2.2 billion " ,

 " what are the lyrics to before he cheats by carrie underwood?" : "And i dug my key into the side of his pretty little suped up four wheel drive", 

 " How many stars are there in the galaxy?" : " 100 to 400 billion stars ",

 " How many animal rescues are there in the world? ": " 4,064 rescues " ,

 "how many people are coffee drinkers in the world? " : " 1 billion people",

 "What is the biggest national park in the US?" : "Wrangell-st. Elias national park" , 

 "What skincare products are used the most in a girls GRWM?" : " Exfoliant, face masks" , 

 "What makeup brand skyrocketed this year in production/popularity?" : " Rare beauty by selena gomez" , 

 "What is the most used way of transit besides driving a car in the US?" : "The bus" ,

 " What popular food is the most consumed in the US?": "French fries", 

 " What are some of the most common bad habits people have?" : " Not enough sleep, unhealthy eating, poor exercise habits, procrastination" , 

 " What is the most picked degree in a college career?" : " Business" , 

 " What season do people like the most?" : " Fall" , 

 " What pet is more popular, dogs or cats? ": " Dogs " , 

 " How many people don’t own a pet?" : " 43%" , 

 " How many hours do students spend in school per year?" : " 1,231 hours" , 

 " What is the biggest issue in public health today?" : " Heart disease and stroke" , 

 " What is the most popular nail/ hair color that the majority of women choose?" : " Nails: baby pink or blush, Hair: black" , 

 " How many people dropout of high school?" : " 1.89 million" , 

 " How many people don’t finish college?" : " 33%" , 

}
questions_to_reveiw= [] 
correct_questions = []
questions= list (flashcards.keys()) 
my_list= random.sample(questions, k=5 )
for question in my_list: 
    response = input (question)
    if response == flashcards [question]: 
        print ("✅") 
        # add question to correct_questions
        correct_questions.append (f"{question}\n{flashcards [question]}")
    else: 
        print (" ❌") 
        questions_to_reveiw.append (f"{question}\n{flashcards [question]}") 

data["questions_to_reveiw"] += questions_to_reveiw
data["correct_questions"] += correct_questions

import json
with open ("data.json", "w") as f:
    json.dump (data,f, indent=2) 

# read from data.json
import json
with open ("data.json", "r") as f:
    d=json.load (f)
# print summary statistics from previous runs of the program

# print("reveiw these questions") 
# for QA in questions_to_reveiw: 
#     print (QA) 

# TODO:
# for each question,
for question in questions:
    # if correct this time:
    question_and_answer = f"{question}\n{flashcards [question]}"
    if  question_and_answer in correct_questions: 
        # count how many times you answered this correctly in the past
        # data["correct_questions"] # list of all past correct questions
        # question_and_answer # current question and answer
        correct_counter= data["correct_questions"].count ( question_and_answer) 
        # print you've answered "How many people don't finish college? " correctly 5 times. Good job!
        print (f"""
you've answered 
{question_and_answer}
correctly {correct_counter} times 
good job!
""") 
    else:
        # count how many times you answered this incorrectly in the past
        incorrect_counter= data["questions_to_reveiw"].count ( question_and_answer) 
        #question_and _answer # current question and answer 
        # print you've answered "how many people don't own a pet? " incorrectly 10 times. Make sure to study this further
        print (f"""
you've answered 
{question_and_answer}
incorrectly {incorrect_counter} times 
make sure to study this further
""") 