def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

def all_pattern(l):
    global n
    ans=0
    for ds in make_divisors(l)[1:]:
        k=n
        while k%ds==0:
            k//=ds
        ans+=(k%ds==1)
    return ans

n=int(input())
print(all_pattern(n)+all_pattern(n-1))