import math
n=int(input())
n1=n
n2=n
k=math.floor(math.log10(n))
ans1,ans2=0,0

for i in range(0,k+1):
    l1=n1%10
    if l1<=5:
        #こっちは多分OK
        ans1+=l1
        n1=n1//10
    else:
        ans1+=(11-l1)
        n1=n1//10
        n1-=1
print(ans1)