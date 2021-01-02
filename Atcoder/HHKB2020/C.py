n=int(input())
p=list(map(int,input().split()))
check=[0]*200001
mi=0
for i in range(n):
    check[p[i]]+=1
    while True:
        if check[mi]>0:
            mi+=1
        else:
            break
    print(mi)