#前から数えてく、どうなってるかは一意に決まる
import collections

n=int(input())
b=[[0,0,0]]
a=[int(i) for i in input().split()]

def my_index(l, x):
    if x in l:
        return l.index(x)
    else:
        return -1

for i in range(n):
    k=my_index(b[-1],a[i])
    if k==-1:
        print(0)
        break
    b.append([b[-1][j]+1 if j==k else b[-1][j] for j in range(3)])
else:
    x=1
    for i in range(n):
        x=x*b[i].count(a[i])%1000000007
    print(x)
