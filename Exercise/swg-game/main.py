import random

user = int(input("0 for Snake, 1 for Water and 2 for Gun: "))

def check(comp, user):
    if comp == user:
        return 0
    elif (comp == 0 and user == 1) or (comp == 1 and user == 2) or (comp == 2 and user == 0):
        return -1
    else:
        return 1
    

comp = random.randint(0, 2)
score =  check(comp , user)
print("computer value: ", comp)
print("user value" , user)

if score == 0:
    print("It's a Tie")
elif score == -1:
    print("You Lose")
else:
    print("You Win")
