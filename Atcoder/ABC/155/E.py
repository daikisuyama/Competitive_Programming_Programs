import math
n=int(input())
n1=n
n2=n
k=math.floor(math.log10(n))
ans1,ans2=0,0
l=n//(10**k)

ans1+=l
n1=n1-(l*(10**k))

ans2+=1
n2=10**(k+1)-n2
l=n2//(10**k)
ans2+=l
n2=n2-(l*(10**k))

for i in range(k-1,-1,-1):
    l1=n1//(10**i)
    if l1<=5:
        #こっちは多分OK
        ans1+=l1
        n1=n1-(l1*(10**i))
    else:
        ans1+=1
        n1=10**(i+1)-n1
        l1=n1//(10**i)
        ans1+=l1
        n1=n1-(l1*(10**i))

for i in range(k-1,-1,-1):
    l2=n2//(10**i)
    if l2<=5:
        #こっちは多分OK
        ans2+=l2
        n2=n2-(l2*(10**i))
    else:
        ans2+=1
        n2=10**(i+1)-n2
        l2=n2//(10**i)
        ans2+=l2
        n2=n2-(l2*(10**i))
print(min(ans1,ans2))