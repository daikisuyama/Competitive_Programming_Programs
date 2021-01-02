n=int(input())
a=list(map(int,input().split()))
mask=0
for i in range(31):
    if [(j>>i)&1 for j in a].count(1)==1:
        mask+=(1<<i)
#最大を求める
ans=[-1,-1]
for i in range(n):
    if ans[0]<(a[i]&mask):
        ans[0]=a[i]&mask
        ans[1]=i
realans=[]
realans.append(a[ans[1]])
for i in range(n):
    if i!=ans[1]:
        realans.append(a[i])
print(" ".join(map(str,realans)))
