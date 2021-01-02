a,b=map(int,input().split())
if a>b:
    print((a+b)//2,(a-b)//2)
else:
    print((a+b)//2,-((b-a)//2))