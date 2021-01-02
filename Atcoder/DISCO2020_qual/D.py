m=int(input())
s=0
t=0
for i in range(m):
    d,c=map(int,input().split())
    s+=d*c
    t+=c
ans=t-1
if s%9!=0:
    ans+=s//9
else:
    ans+=s//9-1
print(ans)