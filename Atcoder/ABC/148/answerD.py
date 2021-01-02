n=int(input())
a=[int(i) for i in input().split()]

l=1
k=0
while k<=n-1:
    for i in range(k,n):
        if a[i]==l:
            l+=1
            k=i+1
            break
    else:
        k=n
if l==1:
    print(-1)
else:
    print(n-l+1)
