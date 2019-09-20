#Asks for name
#imports random fortunes for user to read

import random

fortune = random.randint(1,5)

name1 = input("What is your name? ")
print(name1)
print("Hello" , name1)

fortune1 = ("Today it's up to you to create the peacefulness you long for. ")
fortune2 = ("A friend asks only for your time not your money.")
fortune3 = ("If you refuse to accept anything but the best, you very often get it.")
fortune4 = ("A smile is your passport into the hearts of others.")
fortune5 = ("Hard work pays off in the future, laziness pays off now.")

 
if fortune == 1:
    print(fortune1)
if fortune == 2:
    print(fortune2)
if fortune == 3:
    print(fortune3)
if fortune == 4:
    print(fortune4)
if fortune == 5:
    print(fortune5)


input("\n\nPress the enter key to exit.")
