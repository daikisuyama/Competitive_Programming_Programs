n=int(input())
a=[]
b=[]
for i in range(n):
    s=int(input())
    if s%10==0:
        a.append(s)
    else:
        b.append(s)
b.sort()
if len(b)==0:
    print(0)
else:
    #print(sum(a))
    #print(sum(b[:-1]))
    if sum(b)%10==0:
        print(sum(a)+sum(b[1:]))
    else:
        print(sum(a)+sum(b))
