for _ in range(int(input())):
    a,b,k=map(int,input().split())
    ans=(a-b)*(k//2)
    if k%2==0:
        print(ans)
    else:
        print(ans+a)