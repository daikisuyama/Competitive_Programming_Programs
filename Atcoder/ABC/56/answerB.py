w,a,b=map(int,input().split())
if a<=b<=a+w or a<=b+w<=a+w:
    print(0)
elif b>a+w:
    print(b-a-w)
else:
    print(a-b-w)