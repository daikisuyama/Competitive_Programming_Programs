import itertools
n,k=map(int,input().split())
x=[i for i in range(k)]
t=[list(map(int,input().split())) for i in range(n)]
for i in list(itertools.product(x,repeat=n)):
    bug=0
    for j in range(n):
        x_sub=t[j][i[j]]
        bug=bug^x_sub
    if bug==0:
        print("Found")
        break
else:
    print("Nothing")