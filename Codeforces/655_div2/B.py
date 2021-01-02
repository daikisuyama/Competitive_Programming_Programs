def make_divisors(n):
    divisors=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            divisors.append(i)
            if i!=n//i:
                divisors.append(n//i)
    divisors.sort(reverse=True)
    return divisors
for _ in range(int(input())):
    n=int(input())
    m=make_divisors(n)[1]
    print(m*1,m*(n//m-1))
