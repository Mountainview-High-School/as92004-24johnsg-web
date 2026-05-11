#this is my assesment questionaire 

import time              #this is how i use delays (time.sleep(1))
print("Hi there thank you for particeptating im my quiz")
time.sleep(0.5)            #this is a delay to make the program wait for 0.5 seconds
name=input("Please enter your full name. ")    #this line asks the players name and stores it in a variable called NAME
first_name=name.split(" ")[0]
time.sleep(0.5)
print("Thank you "+first_name)#this line prints thank you and then the name variable to say the participants name
time.sleep(0.5)
print("For this quiz we require you age.")
age=int(input("Please enter your age. "))
if age >=14 :
    print("Sorry "+first_name+", you're too old for this quiz, why don't you check out our 14+ quiz.")
elif age <=7 :
    print("Sorry "+first_name+", you're too young for this quiz, why don't you check out our under 8s quiz.")
    time.sleep(0.5)
else:
    print("In this quiz you will be asked 5 questions on cyber security. ")
    time.sleep(1)
    questions = ["Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do? @ A- Delete the message and try to forget about it. @ B- Keep the text and show an adult you trust. @ C- Text the person back saying somthing mean to them. ",
                 "You find out that someone has posted an embarrassing picture of you online. What should you do? @ A- Tweet that they are and idiot and a looser. @ B- Ask your friends to give the person a hard time. @ C- Tell an adult you trust.",
                 "You want to join an online gaming site, what should you username be? @ A- A nickname. @ B- Your name. @ C- Your email address",
                 "Someone in your class has posted their first video on YouTube and has asked you to comment on it. You don’t think the video is good because the editing is very choppy. What could you comment? @ A- Your video is rubbish! @ B- Man, this is awful! Stick to playing sport or somthing. @ C- Congrats on your first video! Let me know if you’d like any help editing for your next video. ",
                 "Someone in your class is a real bully. Some of the other people in your class say: “Let’s get them back, and spam them with random texts.” What do you reply? @ A- “We shouldn’t be mean to them just because they’re mean to us.” @ B- “Yeah, totally. They’re evil and deserve it!” @ C- “Yes, I think that is a great idea. Maybe they will understand what it feels like, and stop bullying us!”"]
    answers = ["B","C","A","C","A"]
    for i in range(len(questions)):
            guesses = 0
            score = 0
            #print(i)
            print(questions[i].split("@")[0])
            time.sleep(2.5)
            print(questions[i].split("@")[1])
            time.sleep(0.5)
            print(questions[i].split("@")[2])
            time.sleep(0.5)
            print(questions[i].split("@")[3])
            time.sleep(0.5)
            while True:
                question_ask=input("What do you think A, B or C? ").upper()
                if question_ask == answers[i]:
                    score += 10
                    time.sleep(1)
                    print("well done "+first_name+" your score is "+score) #this line dosent work on it next period
                    print(score)
                    break                
                else:
                    guesses += 1
                    time.sleep(1)
                    
                    print(guesses)
                    if guesses == 3:
                        print("Sorry but your out of tries the correct answer is "+answers[i])
                        break 
                    else:
                        print("try again")                    
                        time.sleep(0.5)
            time.sleep(2)
time.sleep(1)
print("Well done "+first_name+" you have finished the quiz i hope you enjoyed it and learnt somthing new!!")
time.sleep(0.5)
print("Your score was ""{add score here}"" please exit the quiz and enjoy your day.")
