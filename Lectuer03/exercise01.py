score01 = int(input("Enter the score for test1: "))
score02 = int(input("Enter the score for test2: "))
score03 = int(input("Enter the score for test3: "))

total = (score01 + score02 + score03) / 3
print("The total score is:", total)

if total >= 90:
    print(" Congratulations! ")
    print(" That is a great score! ")