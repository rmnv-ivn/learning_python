#1st task
N = int(input())
lst = [[1 if a==b else 0 for a in range(N)] for b in range(N) ]
for i in lst:
    print(*i)
#2nd task
import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
lst = [num
       for row in lst_in[::-1]
       for num in row[::-1]]

print(*lst)
#3d task
numbers = [int(a) for a in input().split()]
n = int(len(numbers) ** 0.5)

lst = [[numbers[i*n+j] for j in range(n)] for i in range(n)]

print(lst)
#4th task
t = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!"
    ]
lst = [[row for row in i.split() if len(row)>3] for i in t]
print(lst)
#5th task
import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
A = [[row[i] for row in lst_in] for i in range(len(lst_in[0]))]

for row in A:
    print(*row)