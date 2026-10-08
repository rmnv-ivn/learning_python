#1st task
def start_sum_dec(start=0):
    def sum_dec(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + start
        return wrapper
    return sum_dec


@start_sum_dec(start=5)
def nums_into_sum(nums):
    return sum(list(map(int, nums.split())))


nums = input()
print(nums_into_sum(nums))
#2nd task
def tag_wrapper(tag='h1'):
    def tag_wrapper_string(func):
        def wrapper(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'

        return wrapper

    return tag_wrapper_string


@tag_wrapper(tag='div')
def smaller_string(s):
    return s.lower()


s = input()
print(smaller_string(s))
#3d task
def change_symbols(chars=' !?'):
    def change_symbols_string(func):
        def wrapper(*args, **kwargs):
            s = func(*args, **kwargs)
            s = ''.join(map(lambda x: '-' if x in chars else x, s))
            while '--' in s:
                s = s.replace('--','-')
            return s
        return wrapper
    return change_symbols_string


@change_symbols(chars='?!:;,. ')
def swap_letters(s):
    s = s.lower()
    return ''.join(map(lambda x: t.get(x, x), s))


t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

s = input()
print(swap_letters(s))
#4th task
from functools import wraps

def get_sum_from_list(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return sum(func(*args, **kwargs))
    return wrapper


@get_sum_from_list
def get_list(s):
    '''Функция для формирования списка целых значений'''
    return list(map(int, s.split()))