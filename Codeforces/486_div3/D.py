n=int(input())
x=list(map(int,input().split()))
y=set(x)
ans=[x[0]]
for d in range(31):
    e=2**d
    for i in range(n):
        if x[i]-e in y and x[i]+e in y:
            print(3)
            print(x[i]-e,x[i],x[i]+e)
            exit()
        elif x[i]-e in y:
            ans=[x[i],x[i]-e]
        elif x[i]+e in y:
            ans=[x[i],x[i]+e]
if len(ans)==2:
    print(2)
    print(ans[0],ans[1])
else:
    print(1)
    print(ans[0])