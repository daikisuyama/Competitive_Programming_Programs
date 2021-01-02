#わからない
import math
q=int(input())
for i in range(q):
    a,b=map(int,input().split())
    a,b=sorted([a,b])
    l=math.floor(math.sqrt(a*b))
    m=math.floor((a*b)//l)
    if m>l:
        print(2*l-1)
    elif m==l:
        if a==b:
            print(2*l-2)
        else:
            if m<=l:
                l-=1
                m=math.floor((a*b)//l)
    else:
        if m<=l:
            l-=1
            m=math.floor((a*b)//l)
        print(2*l-1)

