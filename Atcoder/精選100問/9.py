#11/26 8:55~8:58,9:27~9:37
#星座の一つの座標を並行移動してどれかに一致させる
#O(n^2m)
m=int(input())
seiza=[list(map(int,input().split())) for i in range(m)]
n=int(input())
hoshi=[list(map(int,input().split())) for i in range(n)]
#星座の1番目の星がどの星と一致するか
for i in range(n):
    ch=[hoshi[i][0]-seiza[0][0],hoshi[i][1]-seiza[0][1]]
    #それぞれの星について一致するか
    f=True
    for j in range(m):
        now=[seiza[j][0]+ch[0],seiza[j][1]+ch[1]]
        for k in range(n):
            if now==hoshi[k]:
                break
        else:
            f=False
            break
    if f:
        print(ch[0],ch[1])
        break