x,y,z,k=map(int,input().split())
a=sorted([int(i) for i in input().split()])
b=sorted([int(i) for i in input().split()])
c=sorted([int(i) for i in input().split()],reverse=True)
ab=[]
for i in range(x):
    for j in range(y):
        ab.append(a[i]+b[j])
ab.sort(reverse=True)
ab=ab[:k]
l=len(ab)
abc=[]
for i in range(l):
    for j in range(z):
        abc.append(ab[i]+c[j])
abc.sort(reverse=True)
for i in range(k):
    print(abc[i])
