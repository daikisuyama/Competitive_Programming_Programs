n,k=map(int,input().split())
t=[list(map(int,input().split())) for i in range(n)]
from itertools import permutations
ans=0
for perm in permutations(range(1,n)):
    now=[0]+list(perm)+[0]
    co=0
    for i in range(n):
        co+=t[now[i]][now[i+1]]
    if co==k:ans+=1
print(ans)