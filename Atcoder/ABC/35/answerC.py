def int2(k):
    return int(k)-1
n,q=map(int,input().split())
lr=[list(map(int2,input().split())) for i in range(q)]
x=[False]*n
for i in range(q):
    for j in range(lr[i][0],lr[i][1]+1):
        x[j]=not x[j]
print("".join(list(map(str,map(int,x)))))
