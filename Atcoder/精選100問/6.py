#11/25 9:11~9:22
n=int(input())
s=list(map(int,input()))
from itertools import product
ans=0
for now in product(range(10),repeat=3):
    check=0
    for l in range(n):
        if now[check]==s[l]:
            check+=1
            if check==3:
                ans+=1
                break
print(ans)