#1st task
s1=input().lower()
print(s1.replace(s1[1], s1[1].upper()))
#2nd task
s=input()
print(s.count('-'))
#3d task
s=input()
print(s.find('ra'))
#4th task
s=input()
print(s.replace('---','--').replace('--','-'))
#5th task
a,b,c = input().split()
print(a.rjust(3,'0'),b.rjust(3,'0'),c.rjust(3,'0'),sep='\n')
#6th task
s=input()
print(s.count(' ')+1)
#7th task
s=input()
print(s.strip().count(' ')+1)
#8th task
s=input()
print(';'.join(s.split()))