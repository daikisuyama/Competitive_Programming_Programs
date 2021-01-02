n=int(input())
b=list(map(int,input().split()))
a=sorted(b)
s=sum(a)
ans=set()
if a[-2]==a[-1]:
    ma=a[-1]
    for i in range(n):
        if s-a[i]==2*ma:
            ans.add(a[i])
else:
    ma1,ma2=a[-1],a[-2]
    for i in range(n):
        if i==n-1 and s-a[i]==2*ma2:
            ans.add(a[i])
        if i!=n-1 and s-a[i]==2*ma1:
            ans.add(a[i])
realans=[]
for i in range(n):
    if b[i] in ans:
        realans.append(str(i+1))
print(len(realans))
print(" ".join(realans))
