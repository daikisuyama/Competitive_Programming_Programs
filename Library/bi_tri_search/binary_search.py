#二分探索
from operator import floordiv,truediv,truth,not_
'''
domain:= 定義域が整数(0)or実数(1)
searchtype:= T→Fで最大値(0)かF→Tで最小値(1)か
f:= boolを返す関数(単調性が必要)(答えでtrueを返すように) 
l,r:= 探索範囲(l,rはsearchtypeの条件を満たすように)
eps:= 誤差(整数なら1,実数なら誤差指定による)
'''
#答えはvalueに格納
class binary_search:
    def __init__(self,domain,searchtype,f,l,r,eps):
        self.domain=domain
        self.searchtype=searchtype
        self.f=f
        self.l,self.r=l,r
        self.eps=eps
        self.op1=[floordiv,truediv][domain]
        self.op2=[not_,truth][searchtype]
        self.value=self.calc()
    def calc(self):
        while self.r-self.l>self.eps:
            diff=self.op1(self.r-self.l,2)
            bisection=self.l+diff
            if self.op2(self.f(bisection)):
                self.r=bisection
            else:
                self.l=bisection
        return [self.l,self.r][self.searchtype]