#1st task
# здесь объявляйте функцию

writers = input().split()


# здесь продолжайте программу
def most_popular(people, *, case_sens=False):
    if not case_sens:
        people = [i.lower() for i in people]
    d = {x: people.count(x) for x in people}
    index = list(d.values()).index(max(d.values()))
    return list(d.items())[index]


result = most_popular(writers, case_sens=True)
#2nd task
# здесь объявляйте функцию

text = input()
symbols = input()


# здесь продолжайте программу
def count_chars(s, chars, *, return_type=tuple, ignore_case=True):
    res = []
    if ignore_case:
        s = s.lower()
        chars = chars.lower()
    for i in chars:
        res.append(s.count(i))
    return return_type(res)


result = count_chars(text, symbols, return_type=set, ignore_case=False)
#3d task
def merge_dicts(*dicts, ignored_keys=None):
    res = {}
    for i in dicts:
        if ignored_keys:
            i = {k: v for k, v in i.items() if k not in ignored_keys}
        res = {**res, **i}
    return res


goods = merge_dicts(goods1, goods2, goods3, goods4, ignored_keys=('id', 'date', 'cat_id'))
#4th task
def filter_by_length(*names, min_length=0, max_length):
    return [x for x in names if min_length <= len(x) <= max_length]


names_initial = input().split()

names_result = filter_by_length(*names_initial, min_length=5, max_length=9)
#5th task
# здесь объявляйте функцию
def are_anagrams(s1, s2, *, start=0, end=-1, ignore_case=True):
    if ignore_case:
        s1, s2 = s1.lower(), s2.lower()
    if end != -1:
        s1, s2 = s1[start:end], s2[start:end]
    return sorted(s1) == sorted(s2)

words = input().split()

# здесь продолжайте программу
result = are_anagrams(*words, ignore_case=False)