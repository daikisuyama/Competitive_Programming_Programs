n=int(input())
a=list(map(int,input().split()))
s=[a[0]]
for i in range(1,n):
    s.append(s[-1]+a[i])

def f(c,i):
    global n,a,s
    return abs(s[c]-(s[i]-s[c]))

def g(c,i):
    global n,a,s
    return abs((s[c]-s[i])-(s[n-1]-s[c]))

ans=[]
for i in range(1,n-2):
    ans_=[]
    #左側決める
    l,r=0,i
    while l+2<r:
        c1=(l*2+r)//3
        c2=(l+2*r)//3
        if f(c1,i)>f(c2,i):
            l=c1
        else:
            r=c2
    x=sorted([(f(j,i),j) for j in range(l,r+1)])[0][1]
    ans_.append(s[x])
    ans_.append(s[i]-s[x])

    #右側決める
    l,r=i+1,n-1
    while l+2<r:
        c1=(l*2+r)//3
        c2=(l+2*r)//3
        if g(c1,i)>g(c2,i):
            l=c1
        else:
            r=c2
    x=sorted([(g(j,i),j) for j in range(l,r+1)])[0][1]
    ans_.append(s[x]-s[i])
    ans_.append(s[n-1]-s[x])

    ans.append(max(ans_)-min(ans_))
print(min(ans))