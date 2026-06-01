import time             #this import time command imports the delay function to my code
GAME_DELAY = 1          #this variable is a constant
correct_answers = 0     #this sets the correct answers to 0 for the end 
score = 0               #this sets the score to 0 for the end 
print("Hi there thank you for participating in my quiz")#this is a print function it prints what is inside the ("")
time.sleep(GAME_DELAY/2)                                #this is the use of the constant variable for the time sleep function    
name=input("Please enter your full name. ").lstrip()    ##.lstrip() removes the space at the start of the inputted answer
first_name=name.split(" ")[0]                           #.split(" ")[0] splits the name into a list and then selects the first name or anything before the first space 
time.sleep(GAME_DELAY/2)         
print("Thank you "+first_name)                          #this uses the list made before and prints it after saying thank you then the first name or first list item
time.sleep(GAME_DELAY/2)         
print("\n")                                             #this function prints a new line
print("For this quiz we require your age.")
time.sleep(GAME_DELAY/2)          
while True:                                             #this is a while loop asking while the statement below is true if so it breaks out if not it loops back around |
    age_input=input("Please enter your age. ")          #this part of the age is checking for letters or symbols and asks again if there are incorrect inputs           |
    if age_input.isdigit():                             #                                                                                                              |
        age = int(age_input)                            #                                                                                                              |
        break                                           #the break line breaks out of the loop if the statement above is true                                          |
    else:                                               #                                                                                                              |
        print("Sorry, your age contains letters or symbols. Please enter only numbers.")#                                                                              |
if age >=14 :                                                                         #this is the start of the verification checking if the participant is too old or too young |
    print("Sorry "+first_name+", you're too old for this quiz, why don't you check out our 14+ quiz.")#                                                                          |         
elif age <=7 :                                                                                        #                                                                          |  
    print("Sorry "+first_name+", you're too young for this quiz, why don't you check out our under 8s quiz.")#                                                                   |
    time.sleep(GAME_DELAY/2)                                                                                 #                                                                   |
else:                                                                                                        #this is the end of the age verification section now the code continues into the questions
    time.sleep(GAME_DELAY*2)
    print("\n")
    print("In this quiz you will be asked 5 questions on cyber security. ")
    print("\n")         
    time.sleep(GAME_DELAY*2)#these are the questions and there options stored in one big list
    questions = ["Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do? @ A- Delete the message and try to forget about it. @ B- Keep the text and show an adult you trust. @ C- Text the person back saying something mean to them. ",            
                "You find out that someone has posted an embarrassing picture of you online. What should you do? @ A- Tweet that they are an idiot and a loser. @ B- Ask your friends to give the person a hard time. @ C- Tell an adult you trust.",         
                "You want to join an online gaming site, what should you username be? @ A- A nickname. @ B- Your name. @ C- Your email address",
                "Someone in your class has posted their first video on YouTube and has asked you to comment on it. You don’t think the video is good because the editing is very choppy. What could you comment? @ A- Your video is rubbish! @ B- Man, this is awful! Stick to playing sport or something. @ C- Congrats on your first video! Let me know if you’d like any help editing for your next video. ",
                "Someone in your class is a real bully. Some of the other people in your class say: “Let’s get them back, and spam them with random texts.” What do you reply? @ A- “We shouldn’t be mean to them just because they’re mean to us.” @ B- “Yeah, totally. They’re evil and deserve it!” @ C- “Yes, I think that is a great idea. Maybe they will understand what it feels like, and stop bullying us!”"]
    answers = ["B","C","A","C","A"]#these are the correct answers      
    for i in range(len(questions)):#this function allows the program to access each item in the lists above 
            guesses = 0#this sets the guesses to 0, if the participant gets the question wrong they get three attempts to correct it          
            print(questions[i].split("@")[0])#this is the line that prints the question splitting it on the @ symbol 
            time.sleep(GAME_DELAY*2)         
            print(questions[i].split("@")[1])#this is the line that prints option 1      
            time.sleep(GAME_DELAY*2)         
            print(questions[i].split("@")[2])#this is the line that prints option 2    
            time.sleep(GAME_DELAY*2)         
            print(questions[i].split("@")[3])#this is the line that prints option 3        
            time.sleep(GAME_DELAY*2)         
            while guesses<3:#this section checks the answer to see if its correct or has invalid characters |
                question_ask = ""#                                                                          |
                while question_ask not in ["A", "B", "C"]:#                                                 |
                    question_ask = input("What do you think A, B or C? ").upper()#                          |
                    if question_ask not in ["A", "B", "C"]:#                                                |
                        print("Please enter A, B or C.")#                                                   |
                if question_ask == answers[i]:#                                                             |
                    correct_answers += 1#                                                                   |        
                    if guesses <1:#                                                                         |  
                        score += 10#                                                                        |
                    time.sleep(GAME_DELAY)#                                                                 |
                    print("Your total score is "+str(score))#                                               |
                    break#                                                                                  |
                else:#                                                                                      |
                    guesses += 1#this section is where it checks the guesses and if is to many (3) it gives you the answer |
                    time.sleep(GAME_DELAY)#                                                                                |
                    if guesses == 3:#                                                                                      |
                        print("Sorry but you're out of tries the correct answer is "+answers[i])#                          |
                        break#                                                                                             |
                    else:#                                                                                                 |
                        print("Try again.")#                                                                                |
                        time.sleep(GAME_DELAY/2)#                                                                          |
            print("\n")#                                                                                                   | 
            time.sleep(GAME_DELAY*1.5)         
time.sleep(GAME_DELAY)           
if age >=14 :#if the participant is too young or old the quiz stops and doesn't print any questions or answers |          
    print()  #                                                                                                 |
elif age <=7 :#                                                                                                |
    print()         
else:           
    time.sleep(GAME_DELAY)           
    print("Well done "+first_name+" you have finished the quiz, hope you enjoyed it and learnt something new!!")#this is the end of the quiz these last lines say thank you and print the scores and correct answers |    
    time.sleep(GAME_DELAY/2)#                                                                                                                                                                                        |
    print("\n")#                                                                                                                                                                                                     |
    print("Great job!! Your score was "+str(score)+" you got "+str(int(score/10))+"/5 correct first try and "+str(correct_answers)+"/5 correct overall, please exit the quiz and enjoy your day.")#                  | 
