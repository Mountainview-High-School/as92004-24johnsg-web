#this is my assesment questionaire 

import time 

print("Hi there thank you for particeptating im my quiz")
time.sleep(0.5)            #this is a delay do make the program wait for 0.5 seconds
NAME=input("Please enter your full name. ")    #this line asks the players name and stores it in a variable called NAME
FIRSTNAME=NAME.split(" ")[0]
time.sleep(0.5)
print("Thank you "+FIRSTNAME)
time.sleep(0.5)
print("For this quiz we require you age.")
AGE=int(input("Please enter your age. "))
if AGE >=14 :
    print("Sorry "+FIRSTNAME+", you're too old for this quiz, why don't you check out our 14+ quiz.")
elif AGE <=7 :
    print("Sorry "+FIRSTNAME+", you're too young for this quiz, why don't you check out our under 8s quiz.")
    time.sleep(0.5)
else:
    print("Your sweet as to continue. ")