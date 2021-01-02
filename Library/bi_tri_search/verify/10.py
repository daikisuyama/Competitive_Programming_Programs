#三分探索
#狭義に凸or凹の関数に対して極値(最小値or最大値)を求める
#広義に凸or凹であっても求まることはある(傾き0の区間が小さければ)
from operator import floordiv,truediv,truth,not_
from math import log
'''
domain:= 定義域が整数(0)or実数(1)
searchtype:= 狭義に凹で最大値を求めたい(0)or狭義に凸で最小値を求めたい(1)
f:= 最大or最小にしたい値を返す
l,r:= 探索範囲
eps:= 誤差(整数なら2,実数なら誤差指定による)
args:= fの引数(iterable)…f(i,args)という形にして展開する必要がある
'''
#インスタンス変数を増やせばfの引数が増えても対応できます
#答えはvalueに格納
class ternary_search:
    def __init__(self,domain,searchtype,f,l,r,eps,args=None):
        self.domain=domain
        self.searchtype=searchtype
        self.f=f
        self.l,self.r=l,r
        self.iter=int(log((r-l)/eps,1.5))+5
        self.args=args
        self.op1=[floordiv,truediv][domain]
        self.op2=[not_,truth][searchtype]
        self.op3=[max,min][searchtype]
        self.value=self.calc()
    def calc(self):
        for _ in range(self.iter):
            diff=self.op1(self.r-self.l,3)
            trisection1=self.l+diff
            trisection2=self.r-diff
            trisection1_value=self.f(trisection1,self.args)
            trisection2_value=self.f(trisection2,self.args)
            if self.op2(trisection1_value<=trisection2_value):
                self.r=trisection2
            if self.op2(trisection1_value>=trisection2_value):
                self.l=trisection1
        return self.op3([self.l,self.l+self.op1(self.r-self.l,2),self.r],key=lambda x:self.f(x,self.args))

n=int(input())
a=list(map(int,input().split()))
s=[a[0]]
for i in range(1,n):
    s.append(s[-1]+a[i])

def f(c,args):
    i,=args
    return abs(s[c]-(s[i]-s[c]))

def g(c,args):
    i,=args
    return abs((s[c]-s[i])-(s[n-1]-s[c]))

ans=[]
for i in range(1,n-2):
    ans_=[]
    x=ternary_search(0,1,f,0,i,2,[i]).value
    ans_.append(s[x])
    ans_.append(s[i]-s[x])

    x=ternary_search(0,1,g,i+1,n-1,2,[i]).value
    ans_.append(s[x]-s[i])
    ans_.append(s[n-1]-s[x])

    ans.append(max(ans_)-min(ans_))
print(min(ans))