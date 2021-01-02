#x:配列
mod=10**9+7
def multarray(x):
    ret=1
    for i in x:
        ret*=i
        ret%=mod
    return ret

n,k=map(int,input().split())
a=list(map(int,input().split()))

#n==kの場合はかけるだけ
if n==k:
    print(multarray(a))
    exit()

#0以上の数と負の数に分けて格納
ap,am=[],[]
for i in range(n):
    if a[i]>=0:
        ap.append(a[i])
    else:
        am.append(a[i])
#それぞれ絶対値の順番にソート
ap.sort(reverse=True)
am.sort()

#0以上の数のみか正の数のみの場合は先に場合分け
if len(am)==0:
    print(multarray(ap[:k]))
    exit()
if len(ap)==0:
    if k%2==0:
        print(multarray(am[:k]))
    else:
        print(multarray(am[::-1][:k]))
    exit()

#組にして格納する(0以上か負かを記録しておく)
apm2=[]
for i in range(len(am)//2):
    apm2.append((am[2*i]*am[2*i+1],0))
for i in range(len(ap)//2):
    apm2.append((ap[2*i]*ap[2*i+1],1))
apm2.sort(reverse=True)

#0以上の数で次にどこを見るのかをチェックしておく
p=0
ans=[]
for i in range(k//2):
    p+=(2*apm2[i][1])
    ans.append(apm2[i][0])

#Kが偶数の時
if k%2==0:
    print(multarray(ans))
    exit()

ans_cand=[]
#一個増やす場合
if p!=len(ap):
    ans_cand.append(multarray(ans)*ap[p]%mod)
#一個減らして二個増やす場合
if p!=0:
    #減らすindex
    check_i=ans.index(ap[p-1]*ap[p-2])
    #ap[p-1]を減らす操作(0除算を避ける)
    ans[check_i]=ap[p-2]
    ans.append(apm2[k//2][0])
    ans_cand.append(multarray(ans))
print(max(ans_cand))
