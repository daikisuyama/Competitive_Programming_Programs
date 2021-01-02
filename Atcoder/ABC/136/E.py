def make_divisors(n):
    divisors=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            divisors.append(i)
            if i!=n//i:
                divisors.append(n//i)
    #約数の大きい順にソートしたい場合
    divisors.sort(reverse=True)
    return divisors
n,k=map(int,input().split())
a=list(map(int,input().split()))
for i in make_divisors(sum(a)):
    x=[a[j]-(a[j]//i)*i for j in range(n)]
    x.sort(reverse=True)
    s=sum(x)
    compk=0
    for j in range(n):
        if s==0:
            break
        else:
            s-=i
            x[j]-=i
            compk+=abs(x[j])
    if compk<=k:
        print(i)
        break