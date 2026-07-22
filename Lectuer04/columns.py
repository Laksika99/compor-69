import random

print("Random number between 1 and 10:", random.randint(1, 100))
mynumber = random.randint(1, 100)
ntries = 1
yourguess = -1
while ntries < 7 and ____________________ :
    msg = str(ntries) + " >> "
    if (ntries == 6):
        msg = "This is your last chance: "
    yourguess = int(input(msg))
    if ___________________:
        print("Your guess is too low.")