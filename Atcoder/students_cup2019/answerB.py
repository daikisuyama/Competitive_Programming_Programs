n,k=input().split()
n,k=int(n),int(k)

a1=[int(i) for i in input().split()]
b1=[]
for i in range(len(a1)):
    b1.append([sum(x>a1[i] for x in a1[:i]),0])
#print(b1)
l=len(a1)
a1.extend(a1)
#print(a1)
for i in range(l):
    #print(i)
    b1[i][1]=sum(x>a1[i+l] for x in a1[:i+l])

c=0
for i in range(len(b1)):
    c+=(2*b1[i][0]+(k-1)*(b1[i][1]-b1[i][0]))*k//2
    if c>10**9+7:
        c=c%(10**9+7)

print(c)
