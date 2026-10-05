#1st task
get_sq = lambda x: x**2
#2nd task
get_div = lambda a,b: None if b==0 else a/b
#3d task
x = float(input())
m = lambda x: x if x>0 else -x
print(m(x))
#4th task
s = input()
ch = lambda x: 'ra' in x
print(ch(s))
#5th task
def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res


digs = [int(x) for x in input().split()]
lst = filter_lst(digs)
print(*lst)
lst = filter_lst(digs, lambda x: x<0)
print(*lst)
lst = filter_lst(digs, lambda x: x>=0)
print(*lst)
lst = filter_lst(digs, lambda x: 3<=x<=5)
print(*lst)