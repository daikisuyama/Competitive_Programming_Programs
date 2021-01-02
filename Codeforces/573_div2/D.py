n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=["sjfnb","cslnb"]
from collections import Counter
if sum(a)==0:
    print(ans[1])
    exit()
c=Counter(a)
check=0
for i in c:
    if c[i]>=3:
        print(ans[1])
        exit()
    if c[i]==2:
        check+=1
if check>=2:
    print(ans[1])
    exit()
if check==1:
    for i in range(n-1):
        if a[i]==a[i+1]:
            if a[i]==0:
                print(ans[1])
                exit()
            a[i]-=1
            if a[i-1]==a[i]:
                print(ans[1])
                exit()
            ans=ans[::-1]
            break
dif=sum(a)-n*(n-1)//2
print(ans[1-dif%2])