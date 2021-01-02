n=int(input())
d=[]
s1=input()
s2=input()

i=0
while i<n:
    if s1[i]==s2[i]:
        i+=1
        d.append(1)
    else:
        i+=2
        d.append(0)
l=len(d)
if d[0]==0:
    ans=6
else:
    ans=3
for i in range(1,l):
    if d[i-1]==1:
        ans*=2
        ans=ans%1000000007
    elif d[i]==0:
        ans*=3
        ans=ans%1000000007
print(ans)
