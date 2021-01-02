import sys
input=sys.stdin.readline
n,sx,sy=map(int,input().split())
a,b,c,d=0,0,0,0
for i in range(n):
    x,y=map(int,input().split())
    if x<=sx-1:
        a+=1
    elif x>=sx+1:
        b+=1
    if y<=sy-1:
        c+=1
    elif y>=sy+1:
        d+=1
m=max(a,b,c,d)
print(m)
if a==m:
    print(sx-1,sy)
elif b==m:
    print(sx+1,sy)
elif c==m:
    print(sx,sy-1)
else:
    print(sx,sy+1)