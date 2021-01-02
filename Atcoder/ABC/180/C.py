def m():
    n=int(input())
    d=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            d+=[i]
            if i!=n//i:d+=[n//i]
    d.sort()
    return d
for i in m():print(i)