#1st task
def get_nod (a,b):
    if a < b:
        a,b = b,a
    while a%b != 0:
        a = a%b
        a,b = b,a
    return b