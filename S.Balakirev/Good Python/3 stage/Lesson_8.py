#1st task
lst=list(map(int, input().split()))
test = lst[0]!=lst[-1]
lst.append(test)
print(*lst)
#2nd task
cities = ["Москва", "Казань", "Ярославль"]
cities.insert(1, "Ульяновск")
print(*cities)
#3d task
lst = list(input())
lst.remove('+')
lst.remove('7')
lst.insert(0, '8')
lst.remove('-')
lst.remove('-')
print(''.join(lst))
#4th task
lst = input().split()
print(f'{lst[2]} {lst[0][0]}.{lst[1][0]}.')
#5th task
lst = list(map(int, input().split()))
lst.sort()
print(*lst[:3])
#6th task
lst = list(map(int, input().split()))
isOdd = lst.pop(-1)%2 == 1
lst.append(isOdd)
print(*lst)
#7th task
lst = list(map(int, input().split()))
print(lst.count(2))
#8th task
lst = input().split()
lst.sort()
lst.pop(0)
print(*lst)