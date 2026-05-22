#1st task
a, b = map(float, input().split())
b, a = a, b
#2nd task
count, total = map(float, input().split())
count+=2
total-=0.3
#3d task
import math
a, b, c = map(float, input().split())
length = round(math.sqrt(a**2 + b**2 + c**2), 2)
#4th task
digit = int(input())
sum_digit = digit//1000 + digit%1000//100 + digit%100//10 + digit%10
#5th task
a, b, c = map(int, input().split())
p = (a+b+c)/2
sq_tr = math.sqrt(p*(p-a)*(p-b)*(p-c))
#6th task
a, b, alpha = map(float, input().split())
length_c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(alpha))
#7th task
d1, d2, alpha = map(int, input().split())
square = round((d1*d2)/2*math.sin(alpha/180*math.pi),1)
#8th task
x0, y0, x1, y1 = map(float, input().split())
cosalpha = (x0*x1 + y0*y1) / (math.sqrt(x0**2 + y0**2) * math.sqrt(x1**2 + y1**2))
alpha = round(180/math.pi * math.acos(cosalpha),1)