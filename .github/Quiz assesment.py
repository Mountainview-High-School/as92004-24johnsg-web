#this is my assesment questionaire 

import time 

print("Hi there thank you for particeptating im my quiz")
time.sleep(0.5)
NAME=input("Please enter your name. ")
time.sleep(0.5)
print("Thank you "+NAME)
time.sleep(0.5)
print("For this quiz we require you age.")
AGE=int(input("Please enter your age. "))
if AGE >=14 :
    print("Sorry "+NAME+", you're too old for this quiz, why don't you check out our 14+ quiz.")
elif AGE <=7 :
    print("Sorry "+NAME+", you're too young for this quiz, why don't you check out our under 8s quiz.")
else:
    print("Your sweet as to continue. ")