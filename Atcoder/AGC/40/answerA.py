def groupby2(ar):
    a2=[[ar[0],1]]
    for i in range(1,len(ar)):
        if a2[-1][0]==ar[i]:
            a2[-1][1]+=1
        else:
            a2.append([ar[i],1])
    return a2

inf=10000000
S=input()
l=len(S)
a=[inf]*(l+1)
if l==2:
    print(1)
else:
    b=groupby2(list(S))
    l2=len(b)
    if l2==1:
        print(b[0][1]*(b[0][1]+1)//2)
    else:
        c=(b[0][1]*(b[0][1]+1)//2)
        for i in range(l2-1):
            y=b[i]
            x=b[i+1]
            c+=(x[1]*(x[1]+1)//2)
            if x[0]==">":
                c-=min(x[1],y[1])
        print(c)

