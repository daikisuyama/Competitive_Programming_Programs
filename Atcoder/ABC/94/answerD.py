import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
n=int(input())
a=sorted(list(map(int,input().split())))
b=a[n-1]
a.pop(n-1)
ans=0
for i in range(n-1):
    if abs(b/2-a[ans])>abs(b/2-a[i]):
        ans=i
print(str(b)+" "+str(a[ans]))
