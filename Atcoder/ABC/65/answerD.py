import copy
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
b=copy.deepcopy(a)
a.sort(key=lambda x:x[0])
b.sort(key=lambda x:x[1])
#検討もつかない
