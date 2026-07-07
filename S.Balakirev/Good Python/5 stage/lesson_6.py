#1st task
N = int(input())
res = []

for i in range(N):
    l = []
    for j in range(N):
        l.append(1)
    res.append(l)

for i,l in enumerate(res):
    l[N-1] = 5
    print(*l)
#2nd task
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
for i,s in enumerate(lst_in):
    while s.count('  '):
        s = s.replace('  ', ' ')
    s = s.replace(' ', '-')
    lst_in[i] = s
    print(s)
#3d task
n = int(input())

for i in range(2,n):
    flag = True
    for j in range(2,i):
        if i%j==0:
            flag = False
            break
    if flag:
        print(i, end=' ')
#4th task
import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
ans = 'ДА'

for i in range(len(lst_in) - 1):
    for j in range(len(lst_in[i]) - 1):
        if lst_in[i][j] + lst_in[i][j + 1] + lst_in[i + 1][j] + lst_in[i + 1][j + 1] > 1:
            ans = 'НЕТ'
            break

print(ans)
#5th task
import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
ans = 'ДА'

for i in range(len(lst_in)):
    for j in range(i + 1, len(lst_in[i])):
        if lst_in[i][j] != lst_in[j][i]:
            ans = 'НЕТ'
            break

print(ans)
#6th task
nmbrs = list(map(int, input().split()))

for i in range(len(nmbrs)):
    min = i
    for j in range(i + 1, len(nmbrs)):
        if nmbrs[min] > nmbrs[j]:
            min = j
    nmbrs[i], nmbrs[min] = nmbrs[min], nmbrs[i]

print(*nmbrs)
#7th task
nmbrs = list(map(int, input().split()))

for i in range(len(nmbrs) - 1):
    for j in range(1, len(nmbrs)):
        if nmbrs[j - 1] > nmbrs[j]:
            nmbrs[j - 1], nmbrs[j] = nmbrs[j], nmbrs[j - 1]

print(*nmbrs)
#8th task
n = int(input())
value = 64

while n!=0:
    while n>=value:
        n-=value
        print(value, end=' ')
    value//=2