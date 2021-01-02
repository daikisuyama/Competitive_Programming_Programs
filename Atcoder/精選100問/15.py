#11/26 16:11~16:17
n=int(input())
from itertools import permutations
from math import sqrt
towns=[list(map(int,input().split())) for i in range(n)]
ans=0
for p in permutations(range(n)):
    for i in range(n-1):
        ans+=sqrt((towns[p[i+1]][0]-towns[p[i]][0])**2+(towns[p[i+1]][1]-towns[p[i]][1])**2)
for i in range(1,n+1):
    ans/=i
print(ans)
