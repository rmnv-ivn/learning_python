#1st task
m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''
menu = m.split('\n')
choice = int(input())
if choice==1:
    print(menu[0])
elif choice==2:
    print(menu[1])
elif choice==3:
    print(menu[2])
elif choice==4:
    print(menu[3])
elif choice==5:
    print(menu[4])
elif choice==6:
    print(menu[5])
#2nd task
a,b,c = map(int, input().split())
if a > b:
    if b > c:
        print(c)
    else:
        print(b)
else:
    if a > c:
        print(c)
    else:
        print(a)
#3d task
weight = float(input())
if weight<=60:
    print(1)
elif weight<=64:
    print(2)
elif weight<=69:
    print(3)
else:
    print(4)
#4th task
d = int(input())
if d==1:
    print('понедельник')
elif d==2:
    print('вторник')
elif d==3:
    print('среда')
elif d==4:
    print('четверг')
elif d==5:
    print('пятница')
elif d==6:
    print('суббота')
elif d==7:
    print('воскресенье')
#5th task
m = int(input())
if m==2:
    print(28)
elif m<8:
    if m%2==0:
        print(30)
    else:
        print(31)
else:
    if m%2==1:
        print(30)
    else:
        print(31)
#6th task
m,n = map(int, input().split())
prev_m = m
next_m = m
prev_n = n-1
next_n = n+1

if n==1:
    if m<=8 and m%2==0 or m>8 and m%2==1:
        prev_n = 31
        prev_m -= 1
    elif m==3:
        prev_n = 28
        prev_m -= 1
    else:
        prev_n = 30
        prev_m -= 1
elif n==28 and m==2:
    next_n = 1
    next_m += 1
elif n==30 and (m<8 and m%2==0 or m>8 and m%2==1):
    next_n = 1
    next_m += 1
elif n==31:
    next_n = 1
    next_m += 1

print(f'{str(prev_m).rjust(2,'0')}.{str(prev_n).rjust(2,'0')}', f'{str(next_m).rjust(2,'0')}.{str(next_n).rjust(2,'0')}')
#7th task
k = int(input())
if k%7==1:
    print('понедельник')
elif k%7==2:
    print('вторник')
elif k%7==3:
    print('среда')
elif k%7==4:
    print('четверг')
elif k%7==5:
    print('пятница')
elif k%7==6:
    print('суббота')
elif k%7==0:
    print('воскресенье')