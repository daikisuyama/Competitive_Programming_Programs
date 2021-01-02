num=list("0123456789")
a,b=map(int,input().split())
s=input()

for i in range(a+b+1):
    if i!=a:
        if s[i] not in num:
            print("No")
            break
    else:
        if s[i]!="-":
            print("No")
            break
else:
    print("Yes")