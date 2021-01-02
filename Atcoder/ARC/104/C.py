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

#dp[l][r]=([l,r]でotを使う最小)
#一つの陣地になるか
inf=10**12
dp=[[inf]*(2*n) for i in range(2*n)]
for l in range(2*n):
    #rはlより大きい
    for r in range(l+1,2*n):
        dp_sub=0
        #確かにこの区間が存在するか(存在しない場合はすぐbreakに変える(枝かり))
        seglen=(r-l+1)//2
        #区間の長さは奇数(2x+1)
        #その時、中に含まれる区間はx+1の長さ
        if (r-l)%2==1:
            for i in range(l,r-seglen+1):
                #iとi+seglenの組
                if lr[i]!=-1:
                    if lr[i]==i+seglen:
                        pass
                    else:
                        break
                elif lx[i]:
                    if not rx[i+seglen]:
                        dp_sub+=0
                    else:
                        break
                elif rx[i]:
                    break
                else:
                    #i+seglenがrxにあるパターンも
                    if rx[i+seglen]:
                        pass
                    else:
                        #この時だけカードをきる(-1,-1)
                        dp_sub+=1
            #この区間が条件を満たせば
            else:
                dp[l][r]=dp_sub

#ここからDFSで候補があるかを探る
#一つでも見つかればexit
#なければNo
#otが合うかのチェック
#otcがotを超える場合は見る必要ない
def dfs(i,otc):
    if otc>ot:
        return
    if i==2*n:
        if otc==ot:
            print("Yes")
            exit()
        else:
            return
    for j in range(i+1,2*n):
        if dp[i][j]!=inf:
            dfs(j+1,otc+dp[i][j])
dfs(0,0)
print("No")