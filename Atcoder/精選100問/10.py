#11/26 9:46~9:49
n=int(input())
a=list(map(int,input().split()))
q=int(input())
m=list(map(int,input().split()))
check=[0]*2001
for i in range(2**n):
    b=0
    for j in range(n):
        if (i>>j)&1:
            b+=a[j]
    check[b]=1
for i in range(q):
    if check[m[i]]:
        print("yes")
    else:
        print("no")