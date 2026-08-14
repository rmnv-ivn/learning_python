#1st task
def get_sq(x):
    return x**2

a = float(input())
print(get_sq(a))
#2nd task
def is_triangle(x,y,z):
    return x<y+z and y<x+z and z<x+y
#3d task
def is_large(text):
    return len(text) >= 3
#4th task
def is_even(x):
    return x%2 == 0


while (a:=int(input())) != 1:
    if is_even(a):
        print(a)
#5th task
def is_odd(x):
    return x%2 == 1


lst_d = list(map(int, input().split()))
lst = [i for i in lst_d if is_odd(i)]
print(*lst)
#6th task
tp = input().strip()

#здесь продолжайте программу

if tp == "RECT":
    def get_sq(l,w):
        return l*w
else:
    def get_sq(l):
        return l**2
#7th task
def is_long(s):
    return len(s) >= 6


cities = input().split()
lst = [i for i in cities if is_long(i)]
print(*lst)
#8th task
def str_len(s):
    return s, len(s)


cities = input().split()
d = {i:str_len(i)[1] for i in cities}
a = sorted(d, key=d.get)
print(*a)
#9th task
def min_max_multiply(mi, ma):
    return mi*ma


digs = [int(i) for i in input().split()]
print(min_max_multiply(min(digs), max(digs)))