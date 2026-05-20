import time        
game_delay = 1
correct_answers = 0
score = 0           
print("Hi there thank you for particeptating im my quiz")         
time.sleep(game_delay/2)       
name=input("Please enter your full name. ")        
first_name=name.split(" ")[0]           
time.sleep(game_delay/2)         
print("Thank you "+first_name)         
time.sleep(game_delay/2)         
print("For this quiz we require you age.")          
while True:         
    age_input=input("Please enter your age. ")          
    if age_input.isdigit():         
        age = int(age_input)            
        break           
    else:           
        print("sorry your age contains letters or symbols. Please enter only numbers")          
if age >=14 :           
    print("Sorry "+first_name+", you're too old for this quiz, why don't you check out our 14+ quiz.")          
elif age <=7 :          
    print("Sorry "+first_name+", you're too young for this quiz, why don't you check out our under 8s quiz.")           
    time.sleep(game_delay/2)         
else:           
    time.sleep(game_delay)
    print("In this quiz you will be asked 5 questions on cyber security. ")         
    time.sleep(game_delay)           
    questions = ["Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do? @ A- Delete the message and try to forget about it. @ B- Keep the text and show an adult you trust. @ C- Text the person back saying something mean to them. ",            
                "You find out that someone has posted an embarrassing picture of you online. What should you do? @ A- Tweet that they are and idiot and a loser. @ B- Ask your friends to give the person a hard time. @ C- Tell an adult you trust.",         
                "You want to join an online gaming site, what should you username be? @ A- A nickname. @ B- Your name. @ C- Your email address",
                "Someone in your class has posted their first video on YouTube and has asked you to comment on it. You don’t think the video is good because the editing is very choppy. What could you comment? @ A- Your video is rubbish! @ B- Man, this is awful! Stick to playing sport or something. @ C- Congrats on your first video! Let me know if you’d like any help editing for your next video. ",
                "Someone in your class is a real bully. Some of the other people in your class say: “Let’s get them back, and spam them with random texts.” What do you reply? @ A- “We shouldn’t be mean to them just because they’re mean to us.” @ B- “Yeah, totally. They’re evil and deserve it!” @ C- “Yes, I think that is a great idea. Maybe they will understand what it feels like, and stop bullying us!”"]
    answers = ["B","C","A","C","A"]         
    for i in range(len(questions)):         
            guesses = 0         
            print(questions[i].split("@")[0])           
            time.sleep(game_delay*2)         
            print(questions[i].split("@")[1])           
            time.sleep(game_delay*2)         
            print(questions[i].split("@")[2])           
            time.sleep(game_delay*2)         
            print(questions[i].split("@")[3])           
            time.sleep(game_delay*2)         
            while guesses<3:         
                while question_ask not in ["A", "B", "C"]:          
                    print("Please enter A, B or C.")            
                    question_ask = input("What do you think A, B or C? ").upper()        
                if question_ask == answers[i]:          
                    correct_answers += 1
                    if guesses <1:          
                        score += 10         
                    time.sleep(game_delay)           
                    print("Your total score is "+str(score))            
                    break           
                else:           
                    guesses += 1            
                    time.sleep(game_delay)           
                    if guesses == 3:            
                        print("Sorry but you're out of tries the correct answer is "+answers[i])          
                        break           
                    else:           
                        print("try again")          
                        time.sleep(game_delay/2)         
            time.sleep(game_delay*1.5)         
time.sleep(game_delay)           
if age >=14 :           
    print()         
elif age <=7 :          
    print()         
else:           
    time.sleep(game_delay)           
    print("Well done "+first_name+" you have finished the quiz, hope you enjoyed it and learnt something new!!")         
    time.sleep(game_delay/2)         
    print("Great job!! Your score was "+str(score)+" you got "+str(int(score/10))+"/5 correct first try and "+str(correct_answers)+"/5 correct overall, please exit the quiz and enjoy your day.")            
