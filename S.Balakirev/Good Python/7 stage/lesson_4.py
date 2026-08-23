#1st task
def get_rect_value (l,w, tp=0):
    if tp:
        return l*w
    else:
        return (l+w)*2
#2nd task
def check_password (pswrd, chars='$%!?@#'):
    check = False
    if len(pswrd) >= 8:
        for i in pswrd:
            if i in chars:
                check = True
                break
    return check
#3d task
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
    'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
    'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

# здесь продолжайте программу

def krl_change(s, sep='-'):
    res = ''
    s = s.lower()
    for i in s:
        if i in t:
            res+=t[i]
        elif i == ' ':
            res+=sep
        else:
            res+=i
    return res


s = input()
print(krl_change(s))
print(krl_change(s,sep='+'))
#4th task
def wrap_in_tag (s, tag='h1'):
    return f'<{tag}>{s}</{tag}>'


s = input()
print(wrap_in_tag(s))
print(wrap_in_tag(s,tag='div'))
#5th task
def wrap_in_tag_reg (s, tag='h1', up=True):
    if up:
        tag = tag.upper()
    else:
        tag = tag.lower()
    return f'<{tag}>{s}</{tag}>'


s = input()
print(wrap_in_tag_reg(s, tag='div'))
print(wrap_in_tag_reg(s, tag='div', up=False))