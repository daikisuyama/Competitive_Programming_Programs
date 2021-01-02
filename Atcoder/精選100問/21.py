#12:23
n=int(input())
b=[list(map(int,input().split())) for i in range(n)]
def f(x):
    #全てx以下にすることができるか
    #0~n-1
    c=[min(n-1,(x-b[i][0])//(b[i][1])) for i in range(n)]
    c.sort()
    for i in range(n):
        if c[i]<i:
            return False
    return True
#二分探索

from operator import floordiv,truediv,truth,not_
'''
domain:= 定義域が整数(0)or実数(1)
searchtype:= T→Fで最大値(0)かF→Tで最小値(1)か
f:= boolを返す関数(単調性が必要)(答えでtrueを返すように) 
l,r:= 探索範囲(l,rはsearchtypeの条件を満たすように)
eps:= 誤差(整数なら1,実数なら誤差指定による)
'''
#c++にするとオーバフローの可能性があります
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
bs=binary_search(0,1,f,0,10**15,1)
print(bs.value)