for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=[]
    if sum(a)%n!=0:
        print(-1)
        continue
    b=sum(a)//n
    for i in range(1,n):
        if a[i]%(i+1)==0:
            ans.append([i+1,1,a[i]//(i+1)])
            a[0]+=a[i]
            a[i]=0
        else:
            x=i+1-a[i]%(i+1)
            ans.append([1,i+1,x])
            a[0]-=x
            a[i]+=x
            ans.append([i+1,1,a[i]//(i+1)])
            a[0]+=a[i]
            a[i]=0
    for i in range(1,n):
        ans.append([1,i+1,b])
    l=len(ans)
    print(l)
    for i in range(l):
        print(" ".join(map(str,ans[i])))
    