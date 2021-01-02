n,k=map(int,input().split())
a=sorted(list(map(int,input().split())))
def groupby():
    global a
    a2=[[a[0],1]]
    for i in range(1,len(a)):
        if a2[-1][0]==a[i]:
            a2[-1][1]+=1
        else:
            a2.append([a[i],1])
    return a2
b=groupby()
b.sort(key=lambda x:x[1],reverse=True)
l=len(b)
ans=0
for i in range(k,l):
    ans+=b[i][1]
print(ans)