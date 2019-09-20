#Asks for name
#imports random fortunes for user to read

import random

fortune = random.randint(1,8)

name1 = input("What is your name? ")
print(name1)
print("Hello" , name1)

fortune1 = ("Today it's up to you to create the peacefulness you long for. ")
fortune2 = ("A friend asks only for your time not your money.")
fortune3 = ("If you refuse to accept anything but the best, you very often get it.")
fortune4 = ("A smile is your passport into the hearts of others.")
fortune5 = ("Hard work pays off in the future, laziness pays off now.")
fortune6 = ("The fortune you seek is in another cookie.")
fortune7 = ("A conclusion is simply the place where you got tired of thinking.")
fortune8 = ("A dubious friend may be an enemy in camouflage.")
 
if fortune == 1:
    print(fortune1)
elif fortune == 2:
    print(fortune2)
elif fortune == 3:
    print(fortune3)
elif fortune == 4:
    print(fortune4)
elif fortune == 5:
    print(fortune5)
elif fortune == 6:
    print(fortune6)
elif fortune == 7:
    print(fortune7)
elif fortune == 8:
    print(fortune8)
else:
    print("Illegal value!")


input("\n\nPress the enter key to exit.")

