import math
n=int(input())
k=[]
for i in range(3):
    m=int(input())
    if m<=n:
        k.append(m)
k.sort(reverse=True)
l=len(k)
if l==0:
    c=math.ceil(n/3)
    if c<=100:
        print("YES")
    else:
        print("NO")
elif k[0]==n:
    print("NO")
else:
    c=0
    if l==1:
        for i in range(l):
            if (n-k[i])%3==0 or (n-k[i])%3==1:
                c+=((n-k[i])//3)
                n=k[i]+1
            else:
                c+=((n-k[i])//3)
                n=k[i]+2
        c+=math.ceil(n/3)
    else:
        for i in range(l):
            if i!=0 and k[i]+1==k[i-1]:
                continue
            else:
                if (n-k[i])%3==0 or (n-k[i])%3==1:
                    c+=((n-k[i])//3)
                    n=k[i]+1
                else:
                    c+=((n-k[i])//3)
                    n=k[i]+2
        c+=math.ceil(n/3)
        if l==3:
            if k[0]==k[1]+1 and k[1]==k[2]+1:
                c=101
                
    if c<=100:
        print("YES")
    else:
        print("NO")
