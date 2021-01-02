from itertools import combination

n,m=map(int,input().split())
c=len(list(combinations(range(n),m)))
x=100*n+1800*m
y=c*(2**(-m))