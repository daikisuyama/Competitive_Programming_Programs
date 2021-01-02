x=set()
s=int(input())
ans=0
while True:
    ans+=1
    if s in x:
        print(ans)
        break
    x.add(s)
    
    if s%2==0:
        s=s//2
    else:
        s=3*s+1

