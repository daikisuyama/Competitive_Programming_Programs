n,m=map(int,input().split())
ans=0
def make_divisors():
    global n
    divisors=[]
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            divisors.append(i)
            if i!=n//i:
                divisors.append(n//i)
    divisors.sort(reverse=True)
    return divisors
div=make_divisors()#大きい順に並んでる
k=len(div)
ans_=[]
now=0

