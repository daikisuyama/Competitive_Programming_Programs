for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    for j in range(n):
        if a[j]<0:
            break
    for i in range(n):
        if a[i]>0:
            j=max(i+1,j)
            while True:
                if j==n:
                    break
                if a[j]<0:
                    m=min(a[i],-a[j])
                    a[i]-=m
                    a[j]+=m
                    if a[i]==0:
                        break
                j+=1
            if j==n:
                break
    ans=0
    #print(a)
    for i in range(n):
        if a[i]>0:
            ans+=a[i]
    print(ans)

