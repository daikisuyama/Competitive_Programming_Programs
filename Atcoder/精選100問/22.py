#12:38
#10分(問題文の誤読)
p=float(input())
#最小にする関数
def f(x):
    return x+p/(2**(x/1.5))
#三分探索
#狭義に凸or凹の関数に対して極値(最小値or最大値)を求める
#広義に凸or凹であっても求まることはある(傾き0の区間が小さければ)
from operator import floordiv,truediv,gt,lt
'''
domain:= 定義域が整数(0)or実数(1)
searchtype:= 狭義に凸で最大値を求めたい(0)or狭義に凹で最小値を求めたい(1)
f:= 最大or最小にしたい値を返す
l,r:= 探索範囲
eps:= 誤差(整数なら2,実数なら誤差指定による)
'''
#c++にするとオーバフローの可能性があります
#インスタンス変数を増やせばfの引数が増えても対応できます
class ternary_search:
    def __init__(self,domain,searchtype,f,l,r,eps):
        self.domain=domain
        self.searchtype=searchtype
        self.f=f
        self.l,self.r=l,r
        self.eps=eps
        self.op1=[floordiv,truediv][domain]
        self.op2=[gt,lt][searchtype]
        self.value=self.calc()
    def calc(self):
        while self.r-self.l>self.eps:
            diff=self.op1(self.r-self.l,3)
            trisection1=self.l+diff
            trisection2=self.r-diff
            if self.op2(self.f(trisection1),self.f(trisection2)):
                self.r=trisection2
            else:
                self.l=trisection1
        return self.l+1-self.op2(self.f(self.l),self.f(self.l+1))
t=ternary_search(1,1,f,0,100,10**-8)
print(f(t.value))