n_,x_=map(int,input().split())
a=[1]
p=[1]
for i in range(n_):
    a.append(2*a[-1]+3)
    p.append(2*p[-1]+1)

def f(n,x):
    if n==0:
        return 1
    elif x==1:
        return 0
    elif x<=1+a[n-1]:
        return f(n-1,x-1)
    elif x==2+a[n-1]:
        return p[n-1]+1
    elif x<=2+2*a[n-1]:
        return p[n-1]+1+f(n-1,x-2-a[n-1])
    else:
        return 2*p[n-1]+1

print(f(n_,x_))