n,k=map(int,input().split())
#0-indexed
p=[i-1 for i in list(map(int,input().split()))]
c=list(map(int,input().split()))
#1回以上K回以下
ansF=-1000000000000000000
for i in range(n):
    #すでに辿ったもの
    check=[False]*n
    #辿った順番
    turns=[]
    #今
    now=i
    while check[now]==False:
        check[now]=True
        turns.append(now)
        now=p[now]
    #答え(今の)
    ans=0
    #kのうち何回分
    #更新を毎回行う
    spare=turns.index(now)
    if spare>=k:
        for j in range(k):
            ans+=c[turns[j]]
            ansF=max(ans,ansF)
        continue
    for j in range(spare):
        ans+=c[turns[j]]
        ansF=max(ans,ansF)
    turns=turns[spare:]
    spare=k-spare
    #サイクルの長さ
    l=len(turns)
    #サイクルの和(あまりも)
    #サイクルどこで止めるか
    x=0
    for j in range(l):
        x+=c[turns[j]]
    #そもそもサイクル回らない場合
    if spare<=l:
        for j in range(spare):
            ans+=c[turns[j]]
            ansF=max(ans,ansF)
        continue
    #サイクル回した方が良い場合もある
    #最後のサイクルは回さない方が良いパターンも
    if x>=0:
        ans+=(x*(spare//l-1))
        ansF=max(ans,ansF)
        for j in range(l):
            ans+=c[turns[j]]
            ansF=max(ans,ansF)
        for j in range(spare%l):
            ans+=c[turns[j]]
            ansF=max(ans,ansF)
    #サイクル回さない方がいい場合
    else:
        for j in range(l):
            ans+=c[turns[j]]
            ansF=max(ans,ansF)
print(ansF)