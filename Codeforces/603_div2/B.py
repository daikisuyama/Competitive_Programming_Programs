for _ in range(int(input())):
    n=int(input())
    d=dict()
    c=[]
    for i in range(n):
        x=input()
        if x in d:
            d[x]+=1
        else:
            d[x]=1
        c.append(x)
    ans=0
    for i in d:
        ans+=(d[i]-1)
    ansa=[]
    for i in range(n):
        if d[c[i]]==1:
            ansa.append(c[i])
            continue
        for j in range(10):
            x=f"{j}"+c[i][1:]
            if x not in d:
                d[c[i]]-=1
                d[x]=1
                ansa.append(x)
                break
    print(ans)
    for i in range(n):
        print(ansa[i])
    