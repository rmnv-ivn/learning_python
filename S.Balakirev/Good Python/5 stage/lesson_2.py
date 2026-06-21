#1st task
p = [0] * 10

while p.count(1) != 5:
    i = int(input())
    if p[i] == 1:
        continue
    p[i] = 1

print(*p)
#2nd task
res,a = 1, 1

while a != 0:
    a = int(input())
    if a <= 0:
        continue
    res *= a

print(res)
#3d task
cities = input().split()
i = 0
res = 'ДА'

while i < len(cities):
    if len(cities[i]) < 5:
        res = 'НЕТ'
        break
    i += 1

print(res)
#4th task
names = list(map(str.lower, input().split()))
i = 0
res = 'НЕТ'

while i < len(names):
    if names[i][0] == names[i][-1]:
        res = 'ДА'
        break
    i += 1

print(res)
#5th task
n = float(input())
i = 1
res = []

if n < 100:
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            res.append(i)
        i += 1
    else:
        print(*res)
else:
    print('слишком большое значение n')
#6th task
n = float(input())
i = 1

while i<=n:
    if i**2 > n:
        break
    i += 1
print(i)
#7th task
x = float(input())
dpd = 10
i = 1

while dpd<=x:
    dpd *= 1.1
    i += 1
print(i)
#8th task
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
i = 0

while i<len(lst_in):
    if lst_in[i].find(' ') != -1:
        lst_in.pop(i)
        continue
    i += 1

print(*lst_in)