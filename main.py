import random 
flashcards= {
   "How many people use an apple product in the world?" : " 2.2 billion " ,

 " what are the lyrics to before he cheats by carrie underwood?" : "And i dug my key into the side of his pretty little suped up four wheel drive", 

 " How many stars are there in the galaxy?" : " 100 to 400 billion stars ",

 " How many animal rescues are there in the world? ": " 4,064 rescues " ,

 "how many people are coffee drinkers in the world? " : " 1 billion people",
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