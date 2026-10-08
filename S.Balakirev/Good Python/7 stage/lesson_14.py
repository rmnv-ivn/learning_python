#1st task
def func_show(func):
    def func_dec(*args,**kwargs):
        print(f'Площадь прямоугольника: {func(*args,**kwargs)}')
    return func_dec


def get_sq(width, height):
    return width*height
#2nd task
def show_menu(func):
    def show_menu_list(*args, **kwargs):
        lst = func(*args, **kwargs)
        for i, k in enumerate(lst):
            print(f'{i + 1}. {k}')

    return show_menu_list


@show_menu
def get_menu(s):
    return list(s.split())


menu = input()  # чтение пунктов меню (переменную menu не менять)
#3d task
def sort_numbers(func):
    def sorting_list(*args, **kwargs):
        lst = func(*args, **kwargs)
        lst.sort()
        return lst
    return sorting_list


@sort_numbers
def get_list(s):
    return list(map(int, s.split()))


nums = input()
lst = get_list(nums)
print(*lst)
#4th task
def get_dict(func):
    def wrapper(*agrs,**kwargs):
        lst1,lst2 = func(*agrs,**kwargs)
        return {k:lst2[i] for i,k in enumerate(lst1)}
    return wrapper


@get_dict
def get_list(s1,s2):
    lst1 = list(s1.split())
    lst2 = list(s2.split())
    return (lst1,lst2)


s1 = input()
s2 = input()
d = get_list(s1,s2)
print(*sorted(d.items()))
#5th task
def del_dashes(func):
    def wrapper(*args,**kwargs):
        s = func(*args,**kwargs)
        while '--' in s:
            s = s.replace('--', '-')
        return s
    return wrapper


@del_dashes
def modify_string(s):
    s = s.lower()
    return ''.join(map(lambda x: '-' if x in ' : ;.,_' else t.get(x, x), s))


t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

s = input()
res = modify_string(s)
print(res)