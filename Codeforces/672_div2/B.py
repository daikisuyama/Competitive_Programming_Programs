from collections import Counter
for _ in range(int(input())):
    n=int(input())
    x=[0 for i in range(30)]
    l=list(map(int,input().split()))
    for i in l:
        for j in range(29,-1,-1):
            if (i>>j)&1:
                x[j]+=1
                break
    ans=0
    for i in x:
        if i>1:
            ans+=(i*(i-1)//2)
    print(ans)
