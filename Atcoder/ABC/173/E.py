#ちょうどK個
#絶対値の大きいものから選びたい
#正の数を1個選ぶ時,2個選ぶ時,…k個選ぶ時
#絶対値が小さいもの同士または絶対値が大きいもの同士
#負の時は絶対値小さいものk個
mod=10**9+7
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=[]
a3=[]
for i in range(n):
    if a[i]>0:
        b.append((a[i],1))
    elif a[i]<0:
        b.append((a[i],-1))
    else:
        a3.append(a[i])
#絶対値の小さい順
b1=sorted(b,key=lambda x:abs(x))
b2=sorted(b,reverse=True,key=lambda x:abs(x))
ans=[]
if len(a3):
    ans.append(0)
#偶数個選ぶ場合と奇数こ選ぶ場合で分ける
#負の数を偶数個選ぶ場合
#絶対値大きいものから貪欲に選ぶか、その選んだ中で負の数が奇数の場合は一個減らして他のやつを選ぶ
#増やすという可能性も
#偶数の場合はOK
#絶対値小さいものから貪欲に選ぶ(負で最大の時)
#0を選ぶ
if len(b)<k:
    print(0)
    exit()
cand1=b1[:k]
cnt=0
for i in range(k):
    cnt+=(cand1[i][1]==-1)
if cnt%2==0:
    ans=1
    for i in range(k):
        ans*=cand1[i][0]
        ans%=mod
    print(ans)
else:
    cand3=[]
    cnt2=0
    now=0
    for i in range(k):
        now
        if b1[:k]
cand2=b2[:k]
ans2=1
for i in range(k):
    ans2*=cand2[i][0]
ans.append(ans2)