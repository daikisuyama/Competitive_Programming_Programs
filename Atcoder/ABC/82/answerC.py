n=int(input())
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
ans=0
for i in b:
    if i[0]>i[1]:
        ans+=i[1]
    else:
        ans+=(i[1]-i[0])

print(ans)
