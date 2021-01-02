import itertools
n=int(input())
s=dict()
for i in ["M","A","R","C","H"]:
    s[i]=0
for i in range(n):
    _s=input()
    if _s[0] in ["M","A","R","C","H"]:
        s[_s[0]]+=1
s=list(s.items())
ans=0
for i in range(5):
    for j in range(i+1,5):
        for k in range(j+1,5):
            ans+=(s[i][1]*s[j][1]*s[k][1])
print(ans)