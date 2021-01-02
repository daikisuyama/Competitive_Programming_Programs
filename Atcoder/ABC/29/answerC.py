#三進数で考える
n=int(input())
alp=["a","b","c"]
for i in range(3**n):
    ans=""
    k=i
    for j in range(n-1,-1,-1):
        ans+=alp[k//(3**j)]
        k%=(3**j)
    print(ans)
#再帰関数での実装の方が良いかもしれない
