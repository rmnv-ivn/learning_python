#1st task
s = input()
res = []

if 'ра' in s:
    for i in range(len(s)-1):
        if s[i:i+2].lower() == 'ра':
            res.append(i)
else:
    res.append(-1)

print(*res)
#2nd task
tel = input()
flag = 'ДА'

if len(tel) != 16:
    flag = 'НЕТ'
else:
    for i,d in enumerate(tel):
        if i == 0 and d != '+':
            flag = 'НЕТ'
        elif i == 1 and d != '7':
            flag = 'НЕТ'
        elif i == 2 and d != '(':
            flag = 'НЕТ'
        elif i == 6 and d != ')':
            flag = 'НЕТ'
        elif (i == 10 or i == 13) and d != '-':
            flag = 'НЕТ'
        elif (3 <= i <= 5 or 7 <= i <= 9 or 11 <= i <= 12 or 14 <= i <= 15) and not ('0' <= d <= '9'):
            flag = 'НЕТ'

print(flag)
#3d task
nmbrs = list(map(int, input().replace(' ', '').replace('+', ' '). replace('-', ' -').split()))
res = 0

for i,d in enumerate(nmbrs):
    res += d

print(res)
#4th task
digits = list(map(int, input().split()))

for i,d in enumerate(digits):
    digits[i]=pow(d,2)

print(*digits)
#5th task
nums = list(map(int, input().split()))
skipFlag = False

for i,d in enumerate(nums):
    if skipFlag:
        skipFlag = False
        continue
    else:
        nums.insert(i+1,d)
        skipFlag = True

print(*nums)
#6th task
nmbrs = list(map(float, input().split()))
minNum = nmbrs[0]

for i,d in enumerate(nmbrs):
    if d < minNum:
        minNum = d

print(minNum)
#7th task
nmbrs = list(map(float, input().split()))

for i, d in enumerate(nmbrs):
    if d < 0:
        nmbrs[i] = -1.0

print(*nmbrs)