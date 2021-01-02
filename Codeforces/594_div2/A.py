for _ in range(int(input())):
    n=int(input())
    p=list(map(int,input().split()))
    m=int(input())
    q=list(map(int,input().split()))
    co0=0
    for i in range(n):
        co0+=(p[i]%2==0)
    co1=n-co0
    co2=0
    for i in range(m):
        co2+=(q[i]%2==0)
    co3=m-co2
    print(co0*co2+co1*co3)