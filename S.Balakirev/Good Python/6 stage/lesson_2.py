#1st task
lst = [int(i) for i in input().split()]
d = dict.fromkeys(lst)
print(*d.keys())
#2nd task
morze = {'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ё': '.', 'Ж': '...-', 'З': '--..',
         'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.',
         'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-',
         'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-', ' ': '-...-'}

s = input().upper()
message = []

for i in s:
    message.append(morze[i])

print(*message)
#3d task
morze = {'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..', 'И': '..',
         'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...',
         'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-',
         'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-', ' ': '-...-'}
swapped_morze = {v: k.lower() for k, v in morze.items()}

s = input().split()
answer = ''

for i in s:
    answer += swapped_morze[i]

print(answer)
#4th task
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
lst = [[int(j) if j.isdigit() else j for j in i.split()] for i in lst_in]
d = {}

for k, v in lst:
    if d.get(k):
        d[k] += f', {v}'
    else:
        d[k] = v

for k, v in d.items():
    print(f'{k}: {v}')
#5th task
things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
n = int(input()) * 1000
things_back = {k:v for v,k in things.items()}
things_sorted = dict(sorted(things_back.items(), reverse=True))
items = []

for w,i in things_sorted.items():
    if w > n:
        continue
    else:
        n -= w
        items.append(i)

print(*items)