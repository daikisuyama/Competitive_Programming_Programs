s=input()
l=len(s)
se=dict()
k=0
for i in range(l-1,-1,-1):
    k+=(pow(10,l-1-i,2019)*int(s[i]))
    k%=2019
    if k in se:
        se[k]+=1
    else:
        se[k]=1

ans=0
for j in se:
    i=se[j]
    if i>1:
        ans+=(i*(i-1)//2)
    if j==0:
        ans+=i
print(ans)