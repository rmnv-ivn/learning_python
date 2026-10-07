#1st task
def counter_add():
    def counter_inc(x):
        x += 5
        return x

    return counter_inc


cnt = counter_add();
k = int(input())
print(cnt(k))
#2nd task
def counter_add(n):
    def counter_inc(x):
        return x+n
    return counter_inc

cnt = counter_add(2)
k = int(input())
print(cnt(k))
#3d task
def into_header():
    def header_shell(s):
        return f'<h1>{s}</h1>'
    return header_shell

s = input()
h = into_header()
print(h(s))
#4th task
def choose_tag(tag):
    def tag_wrap(s):
        return f'<{tag}>{s}</{tag}>'
    return tag_wrap

tag = input()
s = input()
box = choose_tag(tag)
print(box(s))
#5th task
def collection_type(tp):
    def string_modify(s):
        return list(map(int,s.split())) if tp=='list' else tuple(map(int,s.split()))
    return string_modify

tp = input()
s = input()
lst = collection_type(tp)
print(lst(s))