import copy
n=int(input())
a1=[int(i) for i in input().split()]
a2=copy.deepcopy(a1)
for i in range(1,n):
    a1[i]+=a1[i-1]
for i in range(1,n):
    a2[i]+=a2[i-1]

pm1,c1=0,0
pm2,c2=0,0

for i in range(n):
    a1[i]+=pm1
    if i%2==1:
        if a1[i]>=0:
            pm1-=(a1[i]+1)
            c1+=(a1[i]+1)
    else:
        if a1[i]<=0:
            pm1+=(-a1[i]+1)
            c1+=(-a1[i]+1)

for i in range(n):
    a2[i]+=pm2
    if i%2==0:
        if a2[i]>=0:
            pm2-=(a2[i]+1)
            c2+=(a2[i]+1)
    else:
        if a2[i]<=0:
            pm2+=(-a2[i]+1)
            c2+=(-a2[i]+1)

print(min(c1,c2))
