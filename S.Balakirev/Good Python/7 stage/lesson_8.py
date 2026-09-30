#1st task
def is_right_tr(a, b, c, /, precision=0.001):
    return abs(a ** 2 - (b ** 2 + c ** 2)) < precision or abs(b ** 2 - (a ** 2 + c ** 2)) < precision or abs(
        c ** 2 - (a ** 2 + b ** 2)) < precision


side_a, side_b, side_c = map(float, input().split())

result = is_right_tr(side_a, side_b, side_c)
#2nd task
def verify_password(psw, /, chars='@#!*', min_length=8):
    kir = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    if len(psw) < min_length:
        return False
    for i in psw:
        if i.lower() in kir:
            return False
    for i in psw:
        if i in chars:
            return True
    return False

password = input()

result = verify_password(password, chars="0123456789", min_length=10)
#3d task
def check_phone(phone, format_phone='8(xxx)xxx-xx-xx', /, format_symbol='x'):
    for i, k in enumerate(phone):
        if k != format_phone[i] and format_phone[i] != format_symbol or format_phone[i] == format_symbol and (
                not k.isdigit() or int(k) not in range(10)):
            return False
    return True


phone_number = input()

result = check_phone(phone_number, '+7(***)*** ****', format_symbol='*')
#4th task
DEBUG = 10, 'DEBUG'
INFO = 20, 'INFO'
WARNING = 30, 'WARNING'
ERROR = 40, 'ERROR'
CRITICAL = 50, 'CRITICAL'

def log_event(timestamp, message, /, *, level=INFO, format_log='[%(time)] %(levelname) - %(message)'):
    format_log = format_log.replace('%(time)', str(timestamp))
    format_log = format_log.replace('%(message)', str(message))
    format_log = format_log.replace('%(levelname)', str(level[1]))
    format_log = format_log.replace('%(levelno)', str(level[0]))
    if level[0]>=INFO[0]:
        return format_log
    else:
        return None


log_time = int(input())
log_msg = input()

log_item = log_event(log_time, log_msg, level=WARNING, format_log='%(levelname) - (%(time)) %(message)')
print(log_item)
#5th task
def parser_data(text, /, max_count=0, *, ignore_sign=False):
    text += ' '
    res = []
    signs = ['-', '+']
    first_i = None
    last_i = None

    for i, k in enumerate(text):
        if k.isdigit() and not first_i:
            first_i = i;
        elif not k.isdigit() and first_i:
            last_i = i;

            if not ignore_sign and text[first_i - 1] in signs:
                res.append(text[first_i - 1:last_i])
            else:
                res.append(text[first_i:last_i])

            if len(res) == max_count:
                return res

            first_i = None;
            last_i = None;

    return res


data_text = input()

result = parser_data(data_text, max_count=5, ignore_sign=True)
#6th task
def is_right_rect(a, b, c, d, /, *, precision=0.001):
    points = (a, b, c, d)

    for i, k in enumerate(points):
        a0 = points[(i + 1) % 4][0] - k[0]
        a1 = points[(i + 1) % 4][1] - k[1]
        b0 = points[(i - 1) % 4][0] - k[0]
        b1 = points[(i - 1) % 4][1] - k[1]

        a = (a0 ** 2 + a1 ** 2) ** 0.5
        b = (b0 ** 2 + b1 ** 2) ** 0.5
        cos_alpha = (a0 * b0 + a1 * b1) / (a * b)
        if cos_alpha >= precision:
            return False

    return True


rect_coords = [(float(x.split('=')[0]), float(x.split('=')[1])) for x in input().split()]

result = is_right_rect(*rect_coords)