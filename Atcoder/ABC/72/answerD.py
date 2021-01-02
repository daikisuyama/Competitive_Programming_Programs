n=int(input())
p=[int(i) for i in input().split()]
c=0
for i in range(n-1):
    if p[i]==i+1:
        p[i],p[i+1]=p[i+1],p[i]
        c+=1
if p[-1]==n:
    p[-1],p[-2]=p[-2],p[-1]
    c+=1
print(c)
