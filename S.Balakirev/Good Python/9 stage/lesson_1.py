#1st task
gen = (x for x in range(2,10001))
#2nd task
a, b = map(int, input().split())

tp = tuple((x**2 for x in range(a, b+1)))
#3d task
a, b = map(int, input().split())

gen = (abs(x) for x in range(a,b+1))

for i,x in enumerate(gen):
    if i>4:
        break
    else:
        print(x)
#4th task
a = int(input())
gen1 = (abs(x) for x in range(-a,a+1))
gen2 = (x**3 for x in gen1)

for i,x in enumerate(gen2):
    print(x, end=' ')
    if i==3:
        break
#5th task
from string import ascii_lowercase

gen = (x+y for x in ascii_lowercase for y in ascii_lowercase)

for i,x in enumerate(gen):
    print(x, end=' ')
    if i==49:
        break
#6th task
cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]

gen = (cities[x%len(cities)] for x in range (1000000))
for i,x in enumerate(gen):
    print(x, end=' ')
    if i==19:
        break
#7th task
a,b = map(int, input().split())

gen = (0.5 * pow(x/100, 2) - 2.0 for x in range(a*100,(b+1)*100))

for i,x in enumerate(gen):
    print(round(x,2), end=' ')
    if i==19:
        break