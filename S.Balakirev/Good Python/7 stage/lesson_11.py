#1st task
s = map(float, input().split())
for i in range(3):
    print(next(s), end=' ')
#2nd task
lst = list(map(lambda x: abs(int(x)),input().split()))
print(*lst)
#3d task
s = ''.join(map(lambda x: '#' if x in ['b','i','t','B','I','T'] else x, input()))
print(s)
#4th task
digits = list(map(int, input().split()))
result = list(map(lambda x: x%7==0, digits))
print(*result)
#5th task
s = input()
s_lst = s.split()

tp = tuple(map(lambda x: tuple(x.split('=')), s_lst))
#6th task
cities = list(map(lambda x: '-' if len(x)<=5 else x, input().split()))
print(*cities)
#7th task
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

lst2D = [list(map(int, x.split())) for x in lst_in]
#8th task
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

s = ''.join(map(lambda x: t.get(x, '-'), input().lower()))
print(s)