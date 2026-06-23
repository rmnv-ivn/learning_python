#1st task
print(*list(range(11)))
#2nd task
print(*list(range(-10,1)))
#3d task
print(*list(range(-10,0,2)))
#4th task
print(*list(range(1,20,3)))
#5th task
lst = list(map(int, input().split()))
res = 0

for i in range(len(lst)):
    if lst[i] % 2 != 0:
        res += lst[i]

print(res)
#6th task
n = float(input())
res = 0

for i in range(int(n)):
    if i % 3 == 0 or i % 5 == 0:
        res += i

print(res)
#7th task
cities = input().split()

for i in range(len(cities)):
    cities[i] = len(cities[i])

print(*cities)
#8th task
n = float(input())

for i in range(int(n)+1):
    if i != 0 and int(n)%i == 0:
        print(i)
#9th task
n = float(input())
isSimple = 'ДА'

for i in range(2, int(n)):
    if n % i == 0:
        isSimple = 'НЕТ'
        break

print(isSimple)
#10th task
cities = list(map(str.lower, input().split()))
flag = 'ДА'
lastLit = ''

for i in range(len(cities) - 1):
    lastLit = cities[i][-1]
    if lastLit == 'ь' or lastLit == 'ъ' or lastLit == 'ы':
        lastLit = cities[i][-2]
    if lastLit != cities[i + 1][0]:
        flag = 'НЕТ'

print(flag)