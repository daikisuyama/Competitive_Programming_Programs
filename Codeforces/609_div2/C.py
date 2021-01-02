#題意を全て勘違いしていた
n,k=map(int,input().split())
a=list(map(int,input()))
ans=[-1]*n
upper=-1
lower=-1
#print(a)
#lowerとupperで更新起きるじゃんかす
#更新は起きていいんか、ダメでしょ
for i in range(n-k):
    ans[i]=a[i]
    ans[i+k]=a[i]
    if a[i]==a[i+k]:
        pass
    elif a[i]>a[i+k]:
        #先にupperとなる場合
        if lower==-1 and upper==-1:
            upper=i
    else:
        #先にlowerとなる場合
        if upper==-1 and lower==-1:
            lower=i

if upper==-1 and lower==-1:
    for i in range(n):
        if ans[i]==-1:
            ans[i]=a[i]
    print(n)
    print("".join(map(str,ans)))
    exit()

#upperがTrueのとき(残りの-1は全部合わせればOK)
#upperもっと小さくできないか(無理)
#それ以降ぜろにできるじゃん(できません)
if upper!=-1:
    #-1は全部合わせちゃう
    for i in range(n):
        if ans[i]==-1:
            ans[i]=a[i]
    print(n)
    print("".join(map(str,ans)))
    exit()

#lowerがTrueの場合(-1があるかないか)
if lower!=-1:
    #k-1以前で1だけ大きくしないとlowerになってしまう
    #9の場合は1だけ大きくできない(その場合は前をみる)
    #ただ、前を見て大きくしたときそれより後は0にして良い
    #全部9の場合？(それはいいのでは？)
    #lowerフラッグを変える(大きくする)
    #違うなできるだけ小さいとこで大きくしたいんだ
    for i in range(k-1,-1,-1):
        if i+k>=n:
            if a[i]!=9:
                #+1しちまう
                ans[i]=a[i]+1
                break
        else:
            if a[i]!=9:
                #+1しちまう
                ans[i]+=1
                ans[i+k]+=1
                break
    #iですでに大きいのでそれ以降は0で良い(それよりも前は同じに)
    for j in range(i):
        if ans[j]==-1:
            ans[j]=a[j]
    for j in range(i+1,k):
        ans[j]=0
        if j+k<n:
            ans[j+k]=0
    print(n)
    print("".join(map(str,ans)))
    exit()