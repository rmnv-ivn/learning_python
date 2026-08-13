#1st task
def first_func():
    print("It's my first function")


first_func()
#2nd task
def f():
    name = input()
    print(f'Уважаемый {name}! Вы верно выполнили это задание!')


f()
#3d task
def get_weight(weight):
    print(f'Предмет имеет вес: {weight} кг.')


w = float(input())
get_weight(w)
#4th task
def get_minmax(lst):
    v_min = min(lst)
    v_max = max(lst)
    v_sum = sum(lst)
    print(f'Min = {v_min}, max = {v_max}, sum = {v_sum}')


nums = [int(i) for i in input().split()]
get_minmax(nums)
#5th task
def get_perimeter(width, height):
    perimeter = (width + height) * 2
    print(f'Периметр прямоугольника, равен {perimeter}')


w, h = tuple(int(i) for i in input().split())
get_perimeter(w, h)
#6th task
def email_validation(email):
    values = {'A', 'E', 'I', 'O', 'U', 'Y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S',
              'T', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', 'a', 'e', 'i', 'o',
              'u', 'y', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x',
              'y', 'z', '@', '.'}
    val = False
    if email.count('@') == 1 and email.count('.') == 1 and set(email) < values:
        val = True
    print('ДА' if val else 'НЕТ')


email_validation(input())