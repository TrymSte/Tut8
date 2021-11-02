import random

def 1_6_Dice():
    return random.randint(1,6)

def 2_6_Dice():
    n = 0
    l = []
    while n<=2: 
        l.append(random.randint(1,6))
    return l

def 1_3_Dice():
    return random.randint(1,3)

def 1_10_Dice():
    return random.randint(1,10)


#one must call a function to make this script usefull
