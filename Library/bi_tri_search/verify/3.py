#二分探索
from operator import floordiv,truediv,truth,not_
from math import log
'''
domain:= 定義域が整数(0)or実数(1)
searchtype:= T→Fで最大値(0)かF→Tで最小値(1)か
f:= boolを返す関数(単調性が必要)(答えでtrueを返すように) 
l,r:= 探索範囲(l,rはsearchtypeの条件を満たすように)
eps:= 誤差(整数なら1,実数なら誤差指定による)
args:= fの引数(iterable)…f(i,args)という形にして展開する必要がある
'''
#答えはvalueに格納
class binary_search:
    def __init__(self,domain,searchtype,f,l,r,eps,args=None):
        self.domain=domain
        self.searchtype=searchtype
        self.f=f
        self.args=args
        self.l,self.r=l,r
        self.iter=int(log((r-l)/eps,2.0))+5
        self.op1=[floordiv,truediv][domain]
        self.op2=[not_,truth][searchtype]
        self.value=self.calc()
    def calc(self):
        for _ in range(self.iter):
            diff=self.op1(self.r-self.l,2)
            bisection=self.l+diff
            if self.op2(self.f(bisection,self.args)):
                self.r=bisection
            else:
                self.l=bisection
        return [self.l,self.r][self.searchtype]
n,m=map(int,input().split())
a=[int(input()) for i in range(n)]
b=a[0]
a=sorted(a[1:],reverse=True)
#得られない場合の処理に注意
#スコアの昇順に並べる
#i番目の人と組む,T→F
def f(i,args):
    c=b+a[i]
    if i>=2*m:
        cand=a[:2*m]
    else:
        cand=a[:i]+a[i+1:2*m+1]
    #全部じゃない、どれか一つでも下回ればOK
    for j in range(m):
        d=cand[j]+cand[-1-j]
        if d<=c:
            return True
    return False
#i=0でF,i=n-2でTの場合を先に除く
#n=2*mの場合も
if n==2*m:
    print(a[n-2])
    exit()
if not f(0,None):
    print(-1)
    exit()
if f(n-2,None):
    print(a[n-2])
    exit()
b=binary_search(0,0,f,0,n-1,1)
print(a[b.value])