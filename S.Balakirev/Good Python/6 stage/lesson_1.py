#1st task
lst = [[int(j) if j.isdigit() else j for j in i.split('=')] for i in input().split()]
d = dict(lst)
print(*sorted(d.items()))
#2nd task
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d = {}

for i in lst_in:
    k, v = i.split('=')
    d[int(k)] = v

print(*sorted(d.items()))
#3d task
lst = [[j for j in i.split('=')] for i in input().split()]
d = dict(lst)
if 'house' in d and 'True' in d and '5' in d:
    print('ДА')
else:
    print('НЕТ')
#4th task
lst = [[j for j in i.split('=')] for i in input().split()]
d = dict(lst)
banned = ['False', '3']

for i in banned:
    if i in d:
        del d[i]

print(*sorted(d.items()))
#5th task
lst = input().split()
d = {}

for i in lst:
    if i[:2] not in d:
        d[i[:2]] = []
    d[i[:2]].append(i)

print(*sorted(d.items()))
#6th task
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
lst = [i.split() for i in lst_in]
d = {}

for i in lst:
    if i[1] not in d:
        d[i[1]] = []
        d[i[1]].append(i[0])
    else:
        d[i[1]].append(i[0])

print(*sorted(d.items()))
#7th task
d = {}
while True:
    a = int(input())
    if a == 0:
        break
    elif a not in d:
        d[a] = round(pow(a, 0.5), 2)
        print(d[a])
    else:
        print(f'значение из кэша: {d[a]}')
#8th task
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d = {}

for i in lst_in:
    if i not in d:
        d[i] = f'HTML-страница для адреса {i}'
        print(d[i])
    else:
        print(f'Взято из кэша: {d[i]}')