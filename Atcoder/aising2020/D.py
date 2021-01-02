#0除算
import math
def popcount(x):
    s=0
    y=int(math.log2(x))+2
    for i in range(y):
        if(x>>i)&1:
            s+=1
    return x%s
n=int(input())
x=input()[::-1]
#1がなんこ出るのか
c=x.count("1")
#c+1とc-1だけ考えれば良い
#c=1の時場合分け
#m[i][j]:2^iまで考えたときのmod(c+j-1)
if c!=1:
    m=[[1%(c-1),1%(c+1)]]
    for i in range(n-1):
        m.append([(2*m[-1][0])%(c-1),(2*m[-1][1])%(c+1)])
    l=[0,0]
    for i in range(n):
        if x[i]=="1":
            l[0]+=m[i][0]
            l[1]+=m[i][1]
            l[0]%=(c-1)
            l[1]%=(c+1)
else:
    m=[[1%(c+1),1%(c+1)]]
    for i in range(n-1):
        m.append([(2*m[-1][0])%(c+1),(2*m[-1][1])%(c+1)])
    l=[0,0]
    for i in range(n):
        if x[i]=="1":
            l[0]+=m[i][0]
            l[1]+=m[i][1]
            l[0]%=(c+1)
            l[1]%=(c+1)
#一個だけ変えたいので全体を求める

#最初以外はpopcount使って間に合う
ans=[0]*n
for i in range(n):
    if x[i]=="1":
        if c-1==0:
            ans[i]=0
            continue
        p=(l[0]+(c-1)-m[i][0])%(c-1)
        ans[i]+=1
        while p!=0:
            p=popcount(p)
            ans[i]+=1
    else:
        p=(l[1]+m[i][1])%(c+1)
        ans[i]+=1
        while p!=0:
            p=popcount(p)
            ans[i]+=1
ans=ans[::-1]
for i in range(n):
    print(ans[i])




