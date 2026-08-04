#1st task
s = {float(i) for i in input().split()}

print(*sorted(s))
#2nd task
s = set(i.lower() for i in input().split())
print(len(s))
#3d task
s = set(int(i) for i in input() if i.isdigit())

if len(s):
    print(*sorted(s))
else:
    print('НЕТ')
#4th task
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
print(len(set(lst_in)))
#5th task
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
lst = set(i[:i.index(':')] for i in lst_in)
print(len(lst))
#6th task
cities = set()
city = input()

while city != 'q':
    cities.add(city)
    city = input()

print(len(cities))