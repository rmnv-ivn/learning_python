#1st task
*lst,x,y,z = map(int, input().split())
print(*lst)
#2nd task
cities = input().split()
lst_c = (*cities,)
print(lst_c)
#3d task
a,b = map(int, input().split())
lst = [*range(a,b+1)]
print(*lst)
#4th task
numbers = map(float, input().split())
cities = input().split()
lst = [*numbers, *cities]
print(*lst)
#5th task
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# здесь продолжайте программу (используйте список lst_in и menu)
new_menu = dict(i.split('=') for i in lst_in)
menu = {**menu, **new_menu}