n=int(input())
p=list(map(int,input().split()))
ans=[]
x=[i for i in range(n)]
while True:
    if p[0]!=0:
        ans.append(0)
        q=p[0]
        p[0],p[q]=p[q],p[0]
    else:
        i=p.index(1)
        for j in range(i,n):
            p[j],p[(j+1)%n]=p[(j+1)%n],p[j]
            ans.append(j)
    if p==x:
        break
print(len(ans))
for i in ans:print(i)