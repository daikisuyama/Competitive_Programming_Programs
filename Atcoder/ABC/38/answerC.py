import math
n=int(input())
a=[int(i) for i in input().split()]

def groupby(a):
    a2=[[a[0],1]]
    for i in range(1,len(a)):
        if a2[-1][0]==a[i]:
            a2[-1][1]+=1
        else:
            a2.append([a[i],1])
    return a2

def count_num(k):
    return math.factorial(k)//math.factorial(2)//math.factorial(k-2)

if n==1:
    print(0)
else:
    b=[0]*(n-1)
    for i in range(n-1):
        if a[i]<a[i+1]:
            b[i]=1
    c=groupby(b)
    #print(c)
    d=n
    for i in c:
        if i[0]==1:
            d+=count_num(i[1]+1)
    print(d)
