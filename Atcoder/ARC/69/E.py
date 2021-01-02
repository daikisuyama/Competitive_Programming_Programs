n=int(input())
a=list(map(int,input().split()))
b=[[a[0],0]]
for i in range(1,n):
    if b[-1][0]>=a[i]:
        b.append(b[-1])
    else:
        b.append([a[i],i])
#print(b)
#移る先を考える
cand=[]
now=n-1
while True:
    cand.append(b[now])
    if b[now][1]==0:
        break
    now=b[now][1]-1
cand.append([0,-1])
#print(cand)
c=sorted(a,reverse=True)
#それぞれ上回るものの個数
check=[0]*n
now=0
#print(c)
for i in range(len(cand)-1):
    change=cand[i][1]
    x=cand[i+1][0]
    s=now*(cand[i][0]-cand[i+1][0])
    if now==n:
        check[change]=s
        break
    while c[now]>=x:
        s+=(c[now]-x)
        now+=1
        if now==n:
            break
    check[change]=s
for i in range(n):
    print(check[i])
