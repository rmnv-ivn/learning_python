#1st task
d = int(input())
res = abs(d)
print(res)
#2nd task
d1, d2, d3, d4, d5 = map(int, input().split())
res = min(d1,d2,d3,d4,d5)
print(res)
#3d task
d1, d2, d3, d4, d5 = map(int, input().split())
res = max(d1,d2,d3,d4,d5)
print(res)
#4th task
import math
a, b = map(int, input().split())
length = math.sqrt(a**2 + b**2)
print(length)
#5th task
n, k = map(int, input().split())
Cnk = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
print(Cnk)
#6th task
n, m = map(int, input().split())
total_bus = math.ceil((n+m)/20)
print(total_bus)
#7th task
x = int(input())
res = math.floor(500/(x*0.9))
print(res)