import math

n=int(input())

def get_sieve_of_eratosthenes(n):
    if n==1:
        return []
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

e=get_sieve_of_eratosthenes(n)
l=len(e)

co=1
for i in range(l):
    k=e[i]
    co_sub=1
    l_sub=int(math.log(n,k))
    for j in range(1,l_sub+1):
        co_sub+=n//(k**j)
    co*=co_sub
    co%=(10**9+7)
    #print(co_sub)
print(co)
