n=int(input())
a=list(map(int,input().split()))
ans=0
right=0
np=a[0]
nx=a[0]
for left in range(n):
    while np==nx:
        right+=1
        if right==n:
            break
        np+=a[right]
        nx^=a[right]
    else:
        np-=a[right]
        nx^=a[right]
    right-=1
    ans+=(right-left+1)
    np-=a[left]
    nx^=a[left]
print(ans)