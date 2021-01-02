d=int(input())
c=list(map(int,input().split()))
s=[list(map(int,input().split())) for i in range(d)]
t=[int(input()) for i in range(d)]
ans=0
last=[0]*26
for i in range(d):
    ans+=s[i][t[i]-1]
    last[t[i]-1]=i+1
    for j in range(26):
        ans-=(c[j]*(i+1-last[j]))
    print(ans)