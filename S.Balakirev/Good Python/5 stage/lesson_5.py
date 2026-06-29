#1st task
cities = input().split()
it = iter(cities)
print(next(it))
print(next(it))
#2nd task
s = input()
it = iter(s)
res = ''

for i in range(s.find(' ')):
    res += next(it)

print(res)
#3d task
a = int(input())
s = str(a)
it = iter(s)
res = ''

for i in range(len(s)):
    if i < len(s)-1:
        res += next(it) + ' '
    else:
        res += next(it)

print(res)