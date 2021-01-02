n=int(input())
def modpow():
    ret=1
    for i in range(n-1):
        ret*=2
        ret%=(10**9+7)
    return ret
def perm():
    ret=1
    for i in range(n):
        ret*=(i+1)
        ret%=(10**9+7)
    return ret

print((perm()-modpow())%(10**9+7))