from math import sqrt
def fac(n):
    if n==1:return 0
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return fac(i)+fac(n//i)
    if n%2==1:
        return 1
    else:
        return 0
for _ in range(int(input())):
    ans=["Ashishgup","FastestFinger"]
    n=int(input())
    #print(fac(n)+(n%2==0)+(n%4==0))
    if n==1:
        print(ans[1])
    elif n==2:
        print(ans[0])
    elif n%2==1:
        print(ans[0])
    elif fac(n)==0:
        print(ans[1])
    elif n%4==0:
        print(ans[0])
    else:
        if fac(n)>1:
            print(ans[0])
        else:
            print(ans[1])