l,r=map(int,input().split())
for i in range(l,r+1):
    x=list(str(i))
    y=set(x)
    #print(x,y)
    if len(x)==len(y):
        print(i)
        break
else:
    print(-1)
    