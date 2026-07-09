#1st task
lst = input().split()
lst_abs = [abs(float(x)) for x in lst]
print(lst_abs)
#2nd task
lst = [int(x) for x in input()]
print(lst)
#3d task
cities = [city for city in input().split()
          if len(city) > 5]
print(*cities)
#4th task
n = int(input())
dividers = [x for x in range(1,n+1)
            if n%x == 0]
print(*dividers)
#5th task
N = int(input())
res = [[x]*N for x in range(N)]

for i in res:
    print(*i)
#6th task
lst = [float(x) for x in input().split()]
lst_res = [x for x in lst if int(x)%2 == 0]
print(*lst_res)
#7th task
lst_1 = list(map(int, input().split()))
lst_2 = list(map(int, input().split()))

lst_res = [lst_1[i]+lst_2[i] for i in range(len(lst_1))]

print(*lst_res)
#8th task
info = input().split()

lst = [[info[i], int(info[i+1])] for i in range(0, len(info), 2)]

print(lst)