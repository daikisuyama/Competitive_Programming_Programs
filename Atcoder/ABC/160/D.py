n,x,y=map(int,input().split())
#1→n-1の長さ
ans=[n-i-1 for i in range(n-1)]

k=n-y+x
if k%2==0:
    l=k//2
    l2=min([n-y+1,x])
    for i in range(y-x-1,n-1):
        j=i-y+x+1
        if j+1<=l:
            m=min(l2,j+1)
            ans[j]+=m
            ans[i]-=m
        else:
            m=min(l2,n-i-1)
            ans[j]+=m
            ans[i]-=m
else:
    l=k//2+1
    l2=min([n-y+1,x])
    for i in range(y-x-1,n-1):
        print(ans)
        j=i-y+x+1
        if j+1<=l:
            print(l2)
            print(j+1)
            m=min(l2,j+1)
            #print(m)
            ans[j]+=m
            ans[i]-=m
        else:
            m=min(l2,n-i-1)
            print(l2)
            print(n-i-1)
            ans[j]+=m
            ans[i]-=m
for i in range(n-1):
    print(ans[i])