#1st task
a = float(input())
b = float(input())
d = a if a > b else b
print(d)
#2nd task
num = int(input())
msg = 'кратно 3' if num%3==0 else 'не кратно 3'
print(msg)
#3d task
s = input().lower()
msg = 'палиндром' if s == s[::-1] else 'не палиндром'
print(msg)
#4th task
a = int(input())
msg = 'True' if a==1 else 'False'
print(msg)
#5th task
a = int(input())
msg = 'True' if a==1 else 'False'
print(msg)
#6th task
t = int(input())
t = 0 if t == 59 else t+1
print(t)
#7th task
m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a,b,c = map(int, input().split())
a-=1
b-=1
c-=1
m[a] = f'#{m[a]}' if m[a]=='до' or m[a]=='фа' else m[a]
m[b] = f'#{m[b]}' if m[b]=='до' or m[b]=='фа' else m[b]
m[c] = f'#{m[c]}' if m[c]=='до' or m[c]=='фа' else m[c]
print(m[a],m[b],m[c])