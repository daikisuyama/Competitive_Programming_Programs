n=int(input())
if n%2==1:
    if n==1:
        print(-1)
    else:
        print(1)
elif n%4==0:
    if n==4:
        print(-1)
    else:
        print(1)
else:
    print(-1)