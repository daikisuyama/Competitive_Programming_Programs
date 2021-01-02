n,k=map(int,input().split())
d=dict()
for i in range(k):
    d[i]=0
for i in range(1,n+1):
    d[i%k]+=1
#print(d)
if k%2!=0:
    print(d[0]*d[0]*d[0])
else:
    print(d[0]*d[0]*d[0]+d[k//2]*d[k//2]*d[k//2])


