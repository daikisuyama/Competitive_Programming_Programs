a,b=map(int,input().split())
if a%2==0 and b%2==0:
    k=(b-a)//2
    print(b^(k%2))
elif a%2==0 and b%2==1:
    k=(b-a+1)//2
    print(k%2)
elif a%2==1 and b%2==0:
    k=(b-a-1)//2
    print(a^b^k%2)
else:
    k=(b-a)//2
    print(a^(k%2))