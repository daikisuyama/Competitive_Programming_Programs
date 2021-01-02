#bottomかtopか
n=int(input())
a=list(map(int,input().split()))
an=[]
for i in range(1,n):
    if a[i]>a[i-1]:
        an.append(a[i-1])
        if i==n-1:
            an.append(a[i])
        break
pm=0
for j in range(i+1,n):
    if pm==0:
        if a[j]>=a[j-1]:
            if j==n-1:
                an.append(a[j])
            continue
        else:
            an.append(a[j-1])
            pm=1
    else:
        if a[j]<=a[j-1]:
            continue
        else:
            an.append(a[j-1])
            pm=0
            if j==n-1:
                an.append(a[j])
                
ans=1000
k=0
for i in range(len(an)):
    if i%2==0:
        k=ans//an[i]
        ans-=k*an[i]
    else:
        ans+=k*an[i]
        k=0
print(ans)