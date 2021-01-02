n,m=map(int,input().split())
a=[list(input()) for i in range(n)]
b=[list(input()) for i in range(m)]
def all_true(i,j):
    global a,b
    for k in range(i,i+m):
        for l in range(j,j+m):
            if a[k][l]!=b[k-i][l-j]:
                return False
    return True
f=0
for i in range(n-m+1):
    for j in range(n-m+1):
        if all_true(i,j):
            f=1
            break
    if f==1:
        print("Yes")
        break
else:
    print("No")
