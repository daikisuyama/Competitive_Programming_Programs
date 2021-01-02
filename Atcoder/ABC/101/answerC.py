import math
n,k=map(int,input().split())
a=[int(i) for i in input().split()]

#どうせ最小値になる、最初は最小値
#前から個数数えてく
n-=k
print(math.ceil(n/(k-1))+1)
