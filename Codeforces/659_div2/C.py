for _ in range(int(input())):
    n=int(input())
    a=list(input())
    b=list(input())
    for i in range(n):
        if a[i]>b[i]:
            print(-1)
            break
    else:
        s=sorted(list(set(a)|set(b)))
        ans=0
        for j in s:
            f=False
            x=set()
            for k in range(n):
                if a[k]==j and a[k]!=b[k]:
                    x.add(b[k])
                    f=True
            x=sorted(list(x))
            for k in range(n):
                if a[k]==j and a[k]!=b[k]:
                    a[k]=x[0]
            if f:ans+=1
        print(ans)
