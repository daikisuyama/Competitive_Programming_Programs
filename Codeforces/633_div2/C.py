def need(x):
    ret=1
    y=1
    while y<=x:
        ret+=1
        y*=2
    return ret-1

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    t=0
    for i in range(1,n):
        if a[i]<a[i-1]:
            t=max(t,need(a[i-1]-a[i]))
            a[i]=a[i-1]
            #print(need(a[i-1]-a[i]))
    print(t)