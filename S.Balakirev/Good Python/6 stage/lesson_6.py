#1st task
s = input().split()
d = {int(s[0])+i:v for i,v in enumerate(s[1:])}
print(d[4])
#2nd task
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
lst_unq = {i for i in lst_in}
print(len(lst_unq))
#3d task
res = {s.lower() for s in input().split() if len(s)>=3}
print(len(res))
#4th task
s = input().lower().split()
res = {k:s.count(k) for k in s}
print(res.get('и',0))
#5th task
import sys

# считывание списка из входного потока (список lst_in не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
p = [tuple(j for j in i.split(': ')) for i in lst_in]
d = {k:{v for a,v in p if a==k} for k,v in p}