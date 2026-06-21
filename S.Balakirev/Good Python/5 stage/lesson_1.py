#1st task
n,m = map(int, input().split())
res = ''
while n <= m:
    res += f'{n**2} '
    n += 1
print(res)
#2nd task
price = float(input())
i = 2
res = ''
while i <= 10:
    res += f'{round(price*i, 1)} '
    i += 1
print(res)
#3d task
n = int(input())
s = 0
i = 1
while i<=n:
    s += 1/i
    i += 1
print(round(s,3))
#4th task
a = int(input())
res = 0
while a!=0:
    res += a
    a = int(input())
print(res)
#5th task
s = input()
while s.find('--') != -1:
    s = s.replace('--', '-')
print(s)
#6th task
a = list(input())
i = 0
res = 1
while i<len(a):
    res *= int(a[i])
    i +=1
print(res)
#7th task
n = int(input())
i = 0
fib = [1, 1]
while i<n-2:
    fib.append(fib[i]+fib[i+1])
    i += 1
print(*fib)
#8th task
n = int(input())
i = 3
res = 1
while i<=n:
    res *= 2
    i += 3
print(res)
#9th task
n = int(input())
percent = 5
debt = 1000
i = 1
while i<=n:
    debt*=(1+percent/100)
    i+=1
print(round(debt, 2))
#10th task
n,m = map(int, input().split())
res = []
n = n + (1-n%2)
while n <= m:
    res.append(n)
    n += 2
print(*res)
#11th task
a = 100
res = []
while a<1000:
    if a%47==43 and a%3==0:
        res.append(a)
    a += 1
print(*res)