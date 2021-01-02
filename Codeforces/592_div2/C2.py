from sys import setrecursionlimit
setrecursionlimit(10**8)
from math import gcd
'''
二元一次不定方程式(Binary first-order indefinite equation)
初期化すると、x=x0+m*b,y=y0-m*aで一般解が求められる(初めはm=0)
'''
class InEq:
    #初期化
    def __init__(self,a,b,c):
        self.a,self.b,self.c=a,b,c
        self.m,self.x0,self.y0=0,[0],[0]
        #解が存在するか
        self.check=True
        g=gcd(self.a,self.b)
        if c%g!=0:
            self.check=False
        else:
            #ax+by=gの特殊解
            self.extgcd(self.a,self.b,self.x0,self.y0)
            #ax+by=cの特殊解
            self.x0=self.x0[0]*c//g
            self.y0=self.y0[0]*c//g
            #一般解を求めるために
            self.a//=g
            self.b//=g

    #拡張ユークリッドの互除法
    #返り値:aとbの最大公約数
    def extgcd(self,a,b,x,y):
        if b==0:
            x[0],y[0]=1,0
            return a
        d=self.extgcd(b,a%b,y,x)
        y[0]-=(a//b)*x[0]
        return d

    #パラメータmの更新(xには+bでyには-aの効果)
    def m_update(self,m):
        self.x0+=(m-self.m)*self.b
        self.y0-=(m-self.m)*self.a
        self.m=m

n,p,w,d=map(int,input().split())
eq=InEq(w,d,p)
if not eq.check:
    print(-1)
    exit()
if eq.y0>=0:
    eq.m_update(eq.y0//eq.a)
else:
    eq.m_update(eq.y0//eq.a)
if eq.x0<0 or eq.x0+eq.y0>n:
    print(-1)
else:
    print(eq.x0,eq.y0,n-eq.x0-eq.y0)