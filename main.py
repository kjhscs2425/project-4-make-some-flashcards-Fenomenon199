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
questions= list (flashcards.keys()) 
my_list= random.sample(questions, k=5 )
for question in my_list: 
    response = input (question)
    if response == flashcards [question]: 
        print ("✅") 
    else: 
        print (" ❌") 
        questions_to_reveiw.append (f"{question}\n{flashcards [question]}") 
print("reveiw these questions") 
for QA in questions_to_reveiw: 
    print (QA) 

data["questions_to_reveiw"] += questions_to_reveiw

import json
with open ("data.json", "w") as f:
    json.dump (data,f, indent=2) 
