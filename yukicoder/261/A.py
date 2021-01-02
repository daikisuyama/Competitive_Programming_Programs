def calc(n):
    ret=0
    while n!=0:
        ret+=(n%10)
        n//=10
    return ret
N=int(input())
for i in range(100):
    N=calc(N)
print(N)