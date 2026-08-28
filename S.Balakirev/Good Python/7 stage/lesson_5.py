#1st task
def get_even(*args):
    return [x for x in args if x%2==0]
#2nd task
def get_biggest_city(*args):
    lengths = [len(x) for x in args]
    index = lengths.index(max(lengths))
    return args[index]
#3d task
def get_data_fig(*args, **kwargs):
    p = sum(args)
    res = (p,)
    l = ('tp','color','closed','width')
    for i in l:
        if i in kwargs:
            res += (kwargs[i],)
    return res
#4th task
import sys


# здесь объявляйте функцию
def is_isolate(m, i, j):
    flag = False
    for k in range(-1, 2):
        for l in range(-1, 2):
            if i + k == len(m) or i + k < 0 or j + l == len(m[i]) or j + l < 0:
                continue
            if m[i + k][j + l] == 1 and not (k == 0 and l == 0):
                flag = True
    return flag


def verify(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 1:
                if is_isolate(m, i, j):
                    return False
    return True


lines = sys.stdin.readlines()  # чтение строк из входного потока (переменную lines не менять)
lst2D = [list(map(int, x.strip().split())) for x in lines]  # формирование матрицы чисел
#5th task
def str_min(s1,s2):
    return min(s1,s2)


def str_min3(s1,s2,s3):
    return str_min(str_min(s1,s2),s3)


def str_min4(s1,s2,s3,s4):
    return str_min(str_min(str_min(s1,s2),s3),s4)