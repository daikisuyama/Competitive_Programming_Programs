n=int(input())
ab=[list(map(int,input().split())) for i in range(n)]
ab.sort(reverse=True,key=lambda x:2*x[0]+x[1])
#最初は青木の和,そこから-(2*ai+bi)していって-になった時点
check=sum([i[0] for i in ab])
for i in range(n):
    check-=(2*ab[i][0]+ab[i][1])
    if check<0:
        print(i+1)
        break