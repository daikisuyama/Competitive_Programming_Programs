n=int(input())
#Aに対してのB
#ここを辞書で管理すると遅い
lr,lx,rx,ot=[-1]*(2*n),[0]*(2*n),[0]*(2*n),0
ab=[[j-1 for j in list(map(int,input().split()))] for i in range(n)]

check=[0]*(2*n)
for i in range(n):
    if ab[i][0]!=-2:
        check[ab[i][0]]+=1
    if ab[i][1]!=-2:
        check[ab[i][1]]+=1
    #逆転している場合
    if ab[i][0]!=-2 and ab[i][1]!=-2:
        if ab[i][0]>ab[i][1]:
            print("No")
            exit()

#2個以上含まれる場合
if any(i>1 for i in check):
    print("No")
    exit()

for i in range(n):
    if ab[i][0]==-2 and ab[i][1]==-2:
        ot+=1
    elif ab[i][0]==-2:
        rx[ab[i][1]]=1
    elif ab[i][1]==-2:
        lx[ab[i][0]]=1
    else:
        lr[ab[i][0]]=ab[i][1]

#dp[l][r]=一つの陣地になるか
dp=[[False]*(2*n) for i in range(2*n)]
for l in range(2*n):
    #rはlより大きい
    for r in range(l+1,2*n):
        #確かにこの区間が存在するか(存在しない場合はすぐbreakに変える(枝かり))
        seglen=(r-l+1)//2
        #区間の長さは奇数(2x+1)
        #その時、中に含まれる区間はx+1の長さ
        if (r-l)%2==1:
            for i in range(l,r-seglen+1):
                #lrが異なるか,l,rに間違えて入っているか
                if (lr[i]!=-1 and lr[i]!=i+seglen) or lx[i+seglen] or rx[i]:
                    #print(l,r,1)
                    break
                if lr[i]==i+seglen:
                    continue
                #同時に含まれている場合があるか？
                if [lx[i],rx[i+seglen]].count(True)==2:
                    #print(l,r,2)
                    break
                elif [lx[i],rx[i+seglen]].count(True)==1:
                    continue
            #この区間が条件を満たせば
            else:
                dp[l][r]=True
print(dp)
#ここからは区間DPのマージして最終的にマージしきれたらOK
#dp[l][i],dp[i+1][r]がいずれもTrueならTrue
for l in range(2*n):
    for r in range(l+1,2*n):
        for i in range(l+1,r):
            if dp[l][r]==False:
                if dp[l][i] and dp[i+1][r]:
                    dp[l][r]=True
                    break
#print(dp)
if dp[0][2*n-1]:
    print("Yes")
else:
    print("No")
print(dp)