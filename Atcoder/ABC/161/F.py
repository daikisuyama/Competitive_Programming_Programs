def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors
n=int(input())
x=make_divisors(n)
l=len(x)
ans=0
for i in range(l):
    k=n
    if x[i]==1:
        continue
    while k%x[i]==0:
        k//=x[i]
    if k%x[i]==1:
        ans+=1

y=make_divisors(n-1)
l2=len(y)
ans2=0
for i in range(l2):
    k=n
    if y[i]==1:
        continue
    while k%y[i]==0:
        k//=y[i]
    if k%y[i]==1:
        ans2+=1
print(ans+ans2)


