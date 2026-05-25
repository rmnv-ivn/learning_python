#1st task
a = int(input())
print(int(a%7==0)*100)
#2nd task
a,b,x = map(float, input().split())
res_in = a<=x<b
res_not_in = not a<=x<=b
#3d task
a,b,c,d,x = map(float, input().split())
res_1 = a<x<b or c<=x<=d
res_2 = not a<x<b and c<=x<=d
res_3 = not (a<x<b or c<=x<=d)
#4th task
x0, y0, x1, y1, x, y = map(int, input().split())
is_into_rect = x0<x<x1 and y0<y<y1
is_not_into_rect = not (x0<x<x1 and y0<y<y1)
#5th task
rect_width, rect_height, w, h = map(int, input().split())
total = rect_width//w * bool(rect_height%h) + rect_height//h * bool(rect_width%w) + (bool(rect_height%h) and bool(rect_width%w))
#total = (rect_width % w != 0) * (rect_height // h) + (rect_height % h != 0) * (rect_width // w) + (rect_width % w != 0 and rect_height % h != 0)