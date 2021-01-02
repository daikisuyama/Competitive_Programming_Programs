from collections import Counter
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=Counter(a)
    ans=0
    check=0
    for i in range(101):
        if i not in c:
            if check==1:
                ans+=i
                break
            else:
                ans=2*i
                break
        elif c[i]==1:
            if check==0:
                check+=1
                ans+=i
    print(ans)