for _ in range(int(input())):
    n,t=map(int,input().split())
    a=list(map(int,input().split()))
    ans=[-1]*n
    cand=[]
    for i in range(n):
        if t%2==0:
            if a[i]<t//2:
                ans[i]=0
            elif a[i]>t//2:
                ans[i]=1
            else:
                cand.append(i)
        else:
            if a[i]<=t//2:
                ans[i]=0
            else:
                ans[i]=1
    l=len(cand)
    for i in range(l):
        if i<l//2:
            ans[cand[i]]=0
        else:
            ans[cand[i]]=1
    print(" ".join(map(str,ans)))