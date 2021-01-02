n=int(input())
a=[int(i) for i in input().split()]
s=sum(a)/(len(a)-a.count(0))
if (s-int(s))<10**(-4):
    print(int(s))
else:
    print(int(s)+1)
