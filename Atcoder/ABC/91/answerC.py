n=int(input())
ab=[tuple(map(int,input().split())) for i in range(n)]
cd=[tuple(map(int,input().split())) for i in range(n)]
ab.sort(key=lambda x: x[0]+x[1],reverse=True)
cd.sort(key=lambda x: x[0]+x[1])
check=[False]*n
def isOK(i,j):
    global ab,cd,check
    return ab[i][0]<cd[j][0] and ab[i][1]<cd[j][1]
for i in range(n):
    for j in range(n):
        if not check[j] and isOK(i,j):
            check[j]=True
            break
print(sum(check))

