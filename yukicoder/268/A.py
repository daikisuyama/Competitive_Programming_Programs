n,k=map(int,input().split())
a=list(map(int,input().split()))
b=set(a)
for i in range(k-1,-1,-1):
    if a[i]<=9:
        break
    else:
        if a[i]+1 in b:
            print("No")
            exit()
        if a[i]+3 in b:
            print("No")
            exit()
        if a[i]+5 in b:
            print("No")
            exit()
for j in range(9,0,-1):
    if j in b:
        if j+1 in b:
            if j-3>=1:
                b.add(j-3)
        if j+3 in b:
            if j-2>=1:
                b.add(j-2)
        if j+5 in b:
            if j-1>=1:
                b.add(j-1)
if 1 in b:
    print("No")
    exit()
print("Yes")