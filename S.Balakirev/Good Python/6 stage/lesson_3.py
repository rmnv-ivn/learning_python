#1st task
t = (3.4, -56.7)
numbers = tuple([int(i) for i in input().split()])
t += numbers

print(t)
#2nd task
cities = tuple(input().split())

if 'Москва' not in cities:
    cities += ('Москва',)

print(*cities)
#3d task
cities = input().split()
banned = 'Ульяновск'

if banned in cities:
    banned_index = cities.index(banned)
    cities = cities[:banned_index] + cities[banned_index+1:]

print(*cities)
#4th task
students = tuple(input().split())
res = ()

for i in students:
    i = i.lower()
    if 'ва' in i:
        res += (i,)

print(*res)
#5th task
nums = tuple(int(n) for n in input().split())
res = ()

for i in nums:
    if res.count(i) == 0:
        res += (i,)

print(*res)
#6th task
nums = tuple(int(n) for n in input().split())
res = ()

for i,v in enumerate(nums):
    if nums.count(v) > 1:
        res+= (i,)

print(*res)
#7th task
t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))
n = int(input())
t2 = ()

for i in range(n):
    t_inner = ()
    for j in range(n):
        t_inner += (t[i][j],)
    t2 += (t_inner,)

for i in t2:
    print(*i)
#8th task
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
menu = tuple(tuple(i.split()) for i in lst_in)

print(menu)