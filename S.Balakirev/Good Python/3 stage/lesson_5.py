#1st task
name=input()
surname=input()
age=input()
print("Уважаемый {name} {surname}! Поздравляем Вас с {age}-летием!".format(name=name, surname=surname, age=age))
#2nd task
width,depth,height=input().split()
print("Габариты: {w} x {d} x {h}".format(w=width,d=depth,h=height))
#3d task
a,b=map(int, input().split())
print(min(a,b), max(a,b))
#4th task
city, street, house, apprt = input(), input(), input(), input()
print(f"г. {city}, ул. {street}, д. {house}, кв. {apprt}")
#5th task
import math
dlr, rbls = float(input()), int(input())
print(f"Вы можете получить {math.trunc(rbls/dlr)}$ за {rbls} рублей по курсу {dlr}")