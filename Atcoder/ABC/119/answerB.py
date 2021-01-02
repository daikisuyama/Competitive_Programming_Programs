n=int(input())
c=0
for i in range(n):
    y=input().split()
    if y[1]=="JPY":
        c+=float(y[0])
    else:
        c+=float(y[0])*380000.0

print(c)
