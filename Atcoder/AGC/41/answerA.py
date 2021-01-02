x=[]
n,a,b=map(int,input().split())
if (b-a)%2==0:
    print((b-a)//2)
else:
    c=(a-1)+(b-a+1)//2
    d=(n-b)+(b-a+1)//2
    print(min(c,d))
