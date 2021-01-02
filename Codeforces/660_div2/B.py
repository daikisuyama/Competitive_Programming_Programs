for _ in range(int(input())):
    n=int(input())
    l=n//4 if n%4==0 else n//4+1
    ans="9"*(n-l)+"8"*(l)
    print(ans)