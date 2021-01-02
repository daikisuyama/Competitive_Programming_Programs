from itertools import product
n=int(input())
ans=0
for i in range(3,10):
    l=list(product(["3","5","7"],repeat=i))
    for j in l:
        if len(set(j))==3:
            if int("".join(list(j)))<=n:
                ans+=1
print(ans)