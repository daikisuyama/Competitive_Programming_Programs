p=float(input())

def f(x):
    global p
    return x+p*pow(2,-(x/1.5))

l,r=0,10**18
while l+pow(10,-8)<r:
    c1=l+(r-l)/3
    c2=r-(r-l)/3
    if f(c1)<f(c2):
        r=c2
    else:
        l=c1
        
print(f(l))