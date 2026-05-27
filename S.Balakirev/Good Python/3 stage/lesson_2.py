#1st task
s1 = input()
print(s1[0]+s1[-1])
#2nd task
s1 = input()
print(s1[:4])
#3d task
s1 = input()
print(s1[-3:])
#4th task
s1 = input()
print(s1[1::2])
#5th task
s1 = input()
s2 = input()
print(s1[::2] + ' ' + s2[1::2])
#6th task
s1 = input()
print(s1[4::-1])
#7th task
word1, word2 = input().split()
print(word2[:len(word1)])
#8th task
word1, word2 = input().split()
print(word1[1:len(word2):2] == word2[1::2])