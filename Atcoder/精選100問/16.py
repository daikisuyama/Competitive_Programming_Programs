#11/28 10:32~10:34
#順列を全探索(差を求めるだけ)
n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
from itertools import permutations
ans=0
j=0
for i in permutations(range(1,n+1)):
    j+=1
    if list(i)==p:
        ans+=j
    if list(i)==q:
        ans-=j
print(abs(ans))