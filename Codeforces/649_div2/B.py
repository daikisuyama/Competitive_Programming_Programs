for _ in range(int(input())):
    n=int(input())
    p=list(map(int,input().split()))
    q=[p[0]]
    for i in range(n-1):
        if p[i]!=p[i+1]:
            q.append(p[i+1])
    n=len(q)

    ans=[q[0]]
    for i in range(n-2):
        if q[i]<q[i+1] and q[i+1]>q[i+2]:
            ans.append(q[i+1])
        elif q[i]>q[i+1] and q[i+1]<q[i+2]:
            ans.append(q[i+1])
    ans.append(q[n-1])
    print(len(ans))
    print(" ".join(map(str,ans)))