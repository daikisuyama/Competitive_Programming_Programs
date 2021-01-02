#DPだけどw中心に考えると死ぬ、pを元に考えたい
#は？貪欲にとってくればよさそう？(アホか少ない方が良いやろ)
#二分探索で作れないこともなさそう、いや無理
#仮に最大値の組み合わせがあった時
#(x1+x2+…+xk)/(w1+w2+…+wk)になる
#一個ずつつないでいくのが良いけどな、k,nも小さくて2乗で通るか
#順に一つずつ混ぜるだけか、クソすぎるな

n,k=map(int,input().split())
x=[list(map(int,input().split())) for i in range(n)]
x.sort(key=lambda x:x[1],reverse=True)
check=[0]*n
check[0]=1
#ans1は合計の食塩水、ans2は合計の食塩
ans1,ans2=x[0][0],x[0][0]*x[0][1]/100

for i in range(k-1):
    nex=n
    per=0
    for j in range(n):
        if check[j]==0:
            if (ans1+x[j][0])/(ans2+x[j][0]*x[j][1]/100)>per:
                nex=j
    check[nex]=1
    ans1+=x[nex][0]
    ans2+=x[nex][0]*x[nex][1]/100
print(ans2/ans1*100)
