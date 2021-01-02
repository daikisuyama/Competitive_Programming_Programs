N=int(input())
f=0
for i in range(1,10):
    for j in range(1,10):
        if N==i*j:
            f=1
            break
    if f==1:
        break
if f==0:
    print("No")
else:
    print("Yes")
