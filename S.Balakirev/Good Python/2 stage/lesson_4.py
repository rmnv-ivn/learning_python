#1st task
a = 7
b = -4
c = 3
print (a, b, c)
#2nd task
print(a, b, c, sep="\n")
#3d task
s1 = "Hello"
s2 = "Balakirev"
print(s1, end=" ")
print(s2)
#4th task
s1, s2 = map(str.strip, input().split())
print(f"Word 1: {s1} | Word 2: {s2}")
#5th task
a,b = map(int, input().split())
print(pow(a,b))
#6th task
a,b = map(float, input().split())
print(a+b)
#7th task
x,y = map(int, input().split())
print(x+y+2*x+4*y)
#8th task
a = float(input())
b = float(input())
print(2*(a+b))
#9th task
import math
print(round(math.pi, 3))
#10th task
print(f"Вы ввели число {float(input())}")