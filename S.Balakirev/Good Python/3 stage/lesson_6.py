#1st task
lst = list(map(int, input().split()))
print(lst)
#2nd task
cities = input().split()
print("Москва" in cities)
#3d task
cities = input().split()
print(cities[-1])
#4th task
marks = list(map(int, input().split()))
avg = sum(marks) / len(marks)
print(round(avg, 1))
#5th task
title, author, lists, price = input(), input(), int(input()), float(input())
book = [title, author, lists, price]
del book[2]
book[1] = 'Пушкин'
book[2] *= 2
print(book)
#6th task
viewers = list(map(int, input().split()))
print(max(viewers), min(viewers), sum(viewers))
#7th task
lst = list(map(int, input().split()))
print(*sorted(lst, reverse=True))
#8th task
lst = input().split()
cities = ["Москва", "Тверь", "Вологда"]
print(*(cities+lst))
#9th task
lst = input().split()
cities = ["Москва", "Тверь", "Вологда"]
print(*(lst+cities))