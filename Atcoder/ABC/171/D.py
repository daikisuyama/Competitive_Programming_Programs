n=int(input())
a=dict()
ans=0
for i in map(int,input().split()):
    ans+=i
    if i in a:
        a[i]+=1
    else:
        a[i]=1
q=int(input())
for i in range(q):
    b,c=map(int,input().split())
    if c not in a:
        a[c]=0
    if b not in a:
        a[b]=0
    ans=ans-b*a[b]+c*a[b]
    a[c]+=a[b]
    a[b]=0
    print(ans)