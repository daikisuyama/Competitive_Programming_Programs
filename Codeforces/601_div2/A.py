from itertools import groupby
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[a[i]-b[i] for i in range(n)]
    d=[[i,list(j)] for i,j in groupby(c,key=lambda x:x==0) if i==False]
    if len(d)>=2:
        print("NO")
    elif len(d)==0:
        print("YES")
    else:
        l=len(d[0][1])
        for i in range(l):
            if d[0][1][i]!=d[0][1][0]:
                print("NO")
                break
        else:
            if d[0][1][i]>0:
                print("NO")
            else:
                print("YES")