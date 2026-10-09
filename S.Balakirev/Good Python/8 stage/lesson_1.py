#1st task
import math

a = float(input())
print(math.ceil(a))
#2nd task
from math import floor

a = float(input())
print(floor(a))
#3d task
from math import factorial as fact

def factorial(n):
    p = 1
    for i in range(2, n+1):
        p *= i

    print("my factorial")
    return p
#4th task
from random import seed, randint

seed(1)
print(randint(10,50))
#5th task
from random import seed, random as rnd

seed(10)
print(round(rnd(), 2))