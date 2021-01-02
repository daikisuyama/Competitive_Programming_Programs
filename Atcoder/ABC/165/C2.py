from itertools import combinations_with_replacement
n,m,q=map(int,input().split())
Q=[list(map(int,input().split())) for i in range(q)]
ans=0
for s in combinations_with_replacement(range(1,m+1),n):
    ans_=0
    for k in Q:
        a,b,c,d=k
        if s[b-1]-s[a-1]==c:
            ans_+=d
    ans=max(ans_,ans)
print(ans)