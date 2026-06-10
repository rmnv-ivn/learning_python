#1st task
a,b = map(float, input().split())
if a > b:
    print(a)
else:
    print(b)
#2nd task
str = input().lower()
if str == str[::-1]:
    print('ДА')
else:
    print('НЕТ')
#3d task
m,n = map(int, input().split())
if m%n == 0:
    print(int(m/n))
else:
    print(f'{m} на {n} нацело не делится')
#4th task
a,b,c = map(int, input().split())
if c**2 == a**2 + b**2:
    print('ДА')
else:
    print('НЕТ')
#5th task
number = int(input())
if number % 10 == 7:
    print('ДА')
else:
    print('НЕТ')
#6th task
word = input()
if 't' in word and 'h' in word and 'o' in word:
    print('ДА')
else:
    print('НЕТ')
#7th task
cities = input().split()
if 'Москва' in cities:
    cities.remove('Москва')
print(*cities)
#8th task
a,b,c,d = map(int, input().split())
if (a-c>=2 and b-d>=2) or (a-d>=2 and b-c>=2):
    print('ДА')
else:
    print('НЕТ')
#9th task
number = int(input())
lst = list(map(int, str(number)))
if sum(lst[:3]) == sum(lst[3:]):
    print('ДА')
else:
    print('НЕТ')
#10th task
t = float(input())
if 3<= t%5 <=5:
    print('red')
else:
    print('green')