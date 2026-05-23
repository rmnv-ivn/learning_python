#1st task
import math
a = float(input())
print(math.trunc(a)%3 == 0)
#2nd task
x = float(input())
y = math.modf(x)[0]
print(y>0.5)
#3d task
a, b = map(int, input().split())
print(a%b == 0)
#4th task
a, b, c = map(int, input().split())
print(a+b>c and a+c>b and b+c>a)
#5th task
a = float(input())
print(0<=a<=2 or 10<=a<=20)