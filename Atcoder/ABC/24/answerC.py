n,d,k=map(int,input().split())
LR=[list(map(int,input().split())) for i in range(d)]
ST=[list(map(int,input().split())) for i in range(k)]
#sを今いる場所として動かす？
day=[0]*k
for i in range(d):
    l=LR[i][0]
    r=LR[i][1]
    for j in range(k):
        if ST[j][0]!=ST[j][1]:
            if l <= ST[j][0] <=r:
                if l<= ST[j][1] <=r:
                    ST[j][1]=ST[j][0]
                    day[j]=i+1
                elif ST[j][1]<l:
                    ST[j][0]=l
                else:
                    ST[j][0]=r
for i in range(k):
    print(day[i])
#貪欲法は書きやすいな
