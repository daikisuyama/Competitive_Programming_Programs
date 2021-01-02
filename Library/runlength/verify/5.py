from itertools import groupby
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[[key,group] for key,group in groupby(range(n),key=lambda i:b[i]-a[i]) if key!=0]
    if len(c)>1:
        print("NO")
    elif len(c)==0:
        print("YES")
    else:
        if c[0][0]>0:
            print("YES")
        else:
            print("NO")