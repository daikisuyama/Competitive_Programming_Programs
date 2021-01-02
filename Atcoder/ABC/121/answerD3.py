a,b=map(int,input().split())
if a%2==b%2:
    k=(b-a)//2
    print(b^(k%2) if a%2==0 else a^(k%2))
elif a%2==0 and b%2==1:
    print(((b-a+1)//2)%2)
elif a%2==1 and b%2==0:
    print(a^b^((b-a-1)//2)%2)