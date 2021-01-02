'''
def comb(n,k,p):
  """power_funcを用いて(nCk) mod p を求める"""
  from math import factorial
  if n<0 or k<0 or n<k: return 0
  if n==0 or k==0: return 1
  a=factorial(n) %p
  b=factorial(k) %p
  c=factorial(n-k) %p
  return (a*power_func(b,p-2,p)*power_func(c,p-2,p))%p

def power_func(a,b,p):
  """a^b mod p を求める"""
  if b==0: return 1
  if b%2==0:
    d=power_func(a,b//2,p)
    return d*d %p
  if b%2==1:
    return (a*power_func(a,b-1,p ))%p
'''

def comb_mod(n, r, MOD):
    if n < 0 or r < 0 or n < r:
        return 0

    factrial = [1] * (n+1)
    for k in range(1, n+1):
        factrial[k] = (factrial[k-1] * k) % MOD

    fact_inv = [1] * (n+1)
    fact_inv[n] = pow(factrial[n], MOD - 2, MOD)
    for k in range(n-1, -1, -1):
        fact_inv[k] = (fact_inv[k+1] * (k+1)) % MOD

    return (factrial[n] * fact_inv[r] * fact_inv[n-r]) % MOD

x,y=map(int,input().split())

if (2*y-x)%3!=0 or (2*x-y)%3!=0:
    print(0)
else:
    k=(2*y-x)//3
    l=(2*x-y)//3
    a = comb_mod(k+l,l,10**9+7)
    print(a)
