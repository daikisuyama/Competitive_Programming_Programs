import itertools
n=int(input())
x=list(itertools.permutations([i+1 for i in range(n)]))
p=[int(i) for i in input().split()]
q=[int(i) for i in input().split()]
l=len(x)
a,b=-1,-1
for i in range(l):
    #print(x[i])
    if list(x[i])==p:
        a=i
    if list(x[i])==q:
        b=i
print(abs(a-b))
