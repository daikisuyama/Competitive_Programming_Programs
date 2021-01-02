from fractions import gcd

n=int(input())
a=[int(i) for i in input().split()]
a1=[a[0]]
for i in range(1,n-1):
    a1.append(gcd(a1[-1],a[i]))
a2=[a[-1]]
for i in range(n-2,0,-1):
    a2.append(gcd(a2[-1],a[i]))
m=[]
for i in range(n-2):
    m.append(gcd(a1[i],a2[-i-2]))
m.append(a1[-1])
m.append(a2[-1])
print(max(m))
