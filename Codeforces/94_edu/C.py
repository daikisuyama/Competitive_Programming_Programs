for _ in range(int(input())):
    s=list(map(int,input()))
    x=int(input())
    n=len(s)
    w=[1]*n
    for i in range(n):
        if s[i]==0:
            if i-x>=0:
                w[i-x]=0
            if i+x<n:
                w[i+x]=0
    t=[1]*n
    for i in range(n):
        g=0
        if i-x>=0:
            if w[i-x]==1:
                g+=1
        if i+x<n:
            if w[i+x]==1:
                g+=1
        if g>0:
            t[i]=1
        else:
            t[i]=0
    if s==t:
        print("".join(map(str,w)))
    else:
        print(-1)
