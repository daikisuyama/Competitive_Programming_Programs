from itertools import dropwhile
n=int(input())
a=list(dropwhile(lambda x:x==0,list(map(int,input().split()))[::-1]))[::-1]
n=len(a)
if any(a[i]>i+1 for i in range(n)):
    print("No")
    exit()
c=0
for i in range(n-1,-1,-1):
    if (c+a[i])%(i+1)!=0:
        print("No")
        break
    c+=(c+a[i])//(i+1)
else:
    print("Yes")