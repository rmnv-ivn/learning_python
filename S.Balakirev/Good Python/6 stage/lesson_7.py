#1st task
t = tuple(map(int, input().split()))  # кортеж из целых чисел (в программе не менять)
s = 0  # начальное значение суммы элементов

# здесь продолжайте программу
lst = [s:=s+x for x in t]
print(*lst)
#2nd task
s = 0
while (a:=int(input())) != 0:
    s = s+a if a%2==0 else s+0
print(s)
#3d task
def f(x):
    return abs(x) ** 0.5 + 3.2 + x


t = tuple(map(float, input().split()))  # кортеж t в программе не менять

lst = [[a:=f(x)**i for i in range(1,4)] for x in t]
#4th task
m = 1

while (x := int(input())) > 0:
    m = m * x if x % 3 == 0 else m * 1

print(m)