#なんで？一回飛ばす
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if a==[i+1 for i in range(n)]:
        print(0)
        continue
    #端は除く
    for i in range(n):
        if a[i]!=i+1:
            break
    for j in range(n-1,-1,-1):
        if a[j]!=j+1:
            break
    #インデックス間違い
    for k in range(i,j+1):
        if a[k]==k+1:
            print(2)
            break
    else:
        print(1)