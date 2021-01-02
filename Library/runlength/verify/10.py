#証明は省略しますが直感的には底で買って天井で売れば良いことがわかります
#同じ値段の日が続く場合は無視する
#つまり、(狭義)極小値で買って(狭義)極大値で売れば良い
#初めに極大値が来る場合は1日目に買う
#最後に極小値が来る場合は最終日に売る
from itertools import groupby
n=int(input())
b=list(map(int,input().split()))
a=[b[0]]
for i in range(1,n):
    if a[-1]!=b[i]:
        a.append(b[i])
n=len(a)
#変化ない時
if n==1:
    print(1000)
    exit()
#極小値か極大値かの判定
g=[[key,len(list(group))] for key,group in groupby(range(n-1),key=lambda i:a[i+1]>a[i])]
#買う,売る日を格納する
h=[]
if g[0][0]:
    h.append(0)
now=0
for key,l in g:
    now+=l
    h.append(now)
if not g[-1][0]:
    h.append(n-1)
m,t=1000,0
for i in range(len(h)):
    if i%2==1:
        m+=t*a[h[i]]
        t=0
    else:
        t=m//a[h[i]]
        m%=a[h[i]]
print(m)