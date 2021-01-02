n=input()
l=len(n)
check=[0]*3
for i in range(l):
    check[int(n[i])%3]+=1
if int(n)%3==0:
    print(0)
elif int(n)%3==1:
    if check[1]>=1:
        check[1]-=1
        if sum(check)==0:
            print(-1)
        else:
            print(1)
    else:
        check[2]-=2
        if sum(check)==0:
            print(-1)
        else:
            print(2)
else:
    if check[2]>=1:
        check[2]-=1
        if sum(check)==0:
            print(-1)
        else:
            print(1)
    else:
        check[1]-=2
        if sum(check)==0:
            print(-1)
        else:
            print(2)