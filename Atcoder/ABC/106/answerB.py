def make_divisors(n):
    divisors=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            divisors.append(i)
            if i!=n//i:
                divisors.append(n//i)
    #約数の小さい順にソートしたい場合
    #divisors.sort()
    #約数の大きい順にソートしたい場合
    #divisors.sort(reverse=True)
    return divisors

ans=0
n=int(input())
for i in range(1,n+1):
    ans+=(len(make_divisors(i))==8 and i%2==1)
print(ans)