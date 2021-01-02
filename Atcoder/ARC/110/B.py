n,t=int(input()),input()
if n==1:
    if t=="1":
        print(2*(10**10))
    else:
        print(10**10)
    exit()
if n==2:
    if t=="10" or t=="11":
        print(10**10)
    elif t=="00":
        print(0)
    else:
        print(10**10-1)
    exit()
#以下、nは3以上
x="110"
if t[0:3]=="110":
    for i in range(3,n):
        if t[i]!=x[i%3]:
            print(0)
            exit()
    l=-(-n//3)
    print(10**10-l+1)
elif t[0:3]=="101":
    l=1
    for i in range(2,n):
        if t[i]!=x[(i+1)%3]:
            print(0)
            exit()
    l+=(-(-(n-2)//3))
    print(10**10-l+1)
elif t[0:3]=="011":
    l=1
    for i in range(2,n):
        if t[i]!=x[(i+2)%3]:
            print(0)
            exit()
    l+=(-(-(n-1)//3))
    print(10**10-l+1)
else:
    print(0)