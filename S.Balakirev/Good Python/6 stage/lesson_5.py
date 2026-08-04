#1st task
n1 = tuple(map(int, input().split()))
n2 = tuple(map(int, input().split()))
s = set(n1) & set(n2)
print(*sorted(s))
#2nd task
n1 = tuple(map(int, input().split()))
n2 = tuple(map(int, input().split()))
s = set(n1) - set(n2)
print(*sorted(s))
#3d task
n1 = tuple(map(int, input().split()))
n2 = tuple(map(int, input().split()))
s = set(n1) ^ set(n2)
print(*sorted(s))
#4th task
c1 = tuple(input().split())
c2 = tuple(input().split())
ans = set(c1) == set(c2)
print('ДА' if ans else 'НЕТ')
#5th task
g = set(map(int, input().split()))
print('НЕ ДОПУЩЕН' if 2 in g else 'ДОПУЩЕН')
#6th task
c1 = tuple(input().split())
c2 = tuple(input().split())
ans = set(c2) >= set(c1)
print('ДА' if ans else 'НЕТ')
#7th task
n = int(input())
simple = (2,3,5,7)
q = {2,3,5}
m = ()

for i in simple:
    while n%i == 0:
        n/=i
        m+=(i,)

ans = q <= set(m)
print('ДА' if ans else 'НЕТ')