n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    b.append([a[i],i])
b.sort(reverse=True)
b=[]
for i in range(n):
    b.append([a[i],i])
b.sort(reverse=True)
ans1=[-1 if i!=0 else b[0][0]*b[0][1] for i in range(n)]
ans2=[-1 if i!=n-1 else b[0][0]*abs(b[0][1]-(n-1)) for i in range(n)]
for i in range(1,n):
    mai=[b[i][1],0]
    for j in range(n):
        if ans1[j]==-1:
            if mai[1]<abs(b[i][1]-j):
                mai[0]=j
                mai[1]=abs(b[i][1]-j)
    ans1[mai[0]]=mai[1]*b[i][0]
for i in range(1,n):
    mai=[b[i][1],0]
    for j in range(n):
        if ans2[j]==-1:
            if mai[1]<abs(b[i][1]-j):
                mai[0]=j
                mai[1]=abs(b[i][1]-j)
    ans2[mai[0]]=mai[1]*b[i][0]
print(max(sum(ans1),sum(ans2)))