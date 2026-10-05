#1st task
# считывание числа N
N = int(input())


def get_rec_N(N):
    if N > 1:
        get_rec_N(N - 1)
    print(N)


get_rec_N(N)  # вызов рекурсивной функции
#2nd task
nums = list(map(int, input().split()))

def get_rec_sum(nums, sum=0):
    if len(nums)>0:
        sum = nums.pop() + get_rec_sum(nums, sum)
    return sum


print(get_rec_sum(nums))
#3d task
# ввод числа N
N = int(input())

def fib_rec(N, f):
    if len(f)!=N:
        x = f[-1] + f[-2]
        f.append(x)
        fib_rec(N, f)
    return f

result = fib_rec(N, [1, 1]) # эту строчку не менять
#4th task
n = int(input())

def fact_rec(n):
    if n>1:
        n = n * fact_rec(n-1)
    return 1 if n==0 else n
#5th task
def get_line_list(d,a=None):
    if a is None:
        a = []
    for i in d:
        if type(i)==list:
            get_line_list(i,a)
        else:
            a.append(i)
    return a


d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
#6th task
def get_path(N):
    if N <= 2:
        return N
    return get_path(N - 1) + get_path(N - 2)


N = int(input())
print(get_path(N))
#7th task
def build_up(x, y):
    res = []
    i = 0
    j = 0
    while i < len(x) and j < len(y):
        if x[i] > y[j]:
            res.append(y[j])
            j += 1
        else:
            res.append(x[i])
            i += 1
    res += x[i:] + y[j:]
    return res


def get_sorted(lst):
    split_index = len(lst) // 2
    x = lst[:split_index]
    y = lst[split_index:]

    if len(x) > 1:
        x = get_sorted(x)
    if len(y) > 1:
        y = get_sorted(y)

    return build_up(x, y)


lst = [int(x) for x in input().split()]
print(*get_sorted(lst))