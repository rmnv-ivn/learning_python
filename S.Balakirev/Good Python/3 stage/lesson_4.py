#1st task
s='Тема занятия \"спецсимволы\"'
print(s)
#2nd task
s="\\".join(input().split())
print(s)
#3d task
s="\"".join(input().split()).replace("\"", "\'", 1)
print(s)
#4th task
s=r"C:\WINDOWS\System32\drivers\etc\hosts"
print(s)
#5th task
s=input()
print(f"\"{s}\"")