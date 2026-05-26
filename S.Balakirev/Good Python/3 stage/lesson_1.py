#1st task
s1 = input()
s2 = input()
print(s1+' '+s2)
#2nd task
s1,s2 = input().split()
str = (s1+' ')*2 + (s2+' ')*3
print(str)
#3d task
a,b = input().split()
print("Переменная a = " + str(a) + ", переменная b = " + str(b))
#4th task
s1 = input()
new_s1 = 'Строка: ' + s1 + '. Длина: ' + str(len(s1))
print(new_s1)
#5th task
s1, s2 = input().split()
first = s1 in s2
second = s1 == s2
third = s1 > s2
fourth = s1 < s2
print(first, second, third, fourth)
#6th task
a,b = input().split()
print('Коды: '+a+' = '+ str(ord(a)) +', '+b+' = '+ str(ord(b)))