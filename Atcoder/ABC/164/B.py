a,b,c,d=map(int,input().split())
check=True
while True:
    if check:
        c-=b
        if c<=0:
            print("Yes")
            break
    else:
        a-=d
        if a<=0:
            print("No")
            break
    check=not check