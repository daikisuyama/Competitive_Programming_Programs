#繰り返し二乗法
#枝刈り
a,r,n=map(int,input().split())
def pow(x,n):
    global a
    ans=a
    while n:
        if n%2:
            ans*=x
        x*=x
        n>>=1
        if ans>10**9:
            return "large"
    return ans
print(pow(r,n-1))