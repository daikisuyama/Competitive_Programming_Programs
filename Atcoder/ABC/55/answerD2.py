n=int(input())
s=input()
x=["SS","SW","WS","WW"]

def check(i,j):
    if x[i][j]=="S":
        if s[j]=="o":
            if x[i][j-1]=="S":
                return x[i][j+1]=="S"
            else:
                return x[i][j+1]=="W"
        else:
            if x[i][j-1]=="S":
                return x[i][j+1]=="W"
            else:
                return x[i][j+1]=="S"
    else:
        if s[j]=="o":
            if x[i][j-1]=="S":
                return x[i][j+1]=="W"
            else:
                return x[i][j+1]=="S"
        else:
            if x[i][j-1]=="S":
                return x[i][j+1]=="S"
            else:
                return x[i][j+1]=="W"

a=["S","W"]
for i in range(4):
    for j in range(n-2):
        if x[i][j+1]=="S":
            if s[j+1]=="o":
                x[i]+=a[x[i][j]!="S"]
            else:
                x[i]+=a[x[i][j]=="S"]
        else:
            if s[j+1]=="o":
                x[i]+=a[x[i][j]=="S"]
            else:
                x[i]+=a[x[i][j]!="S"]
    if check(i,0) and check(i,-1):
        print(x[i])
        break
else:
    print(-1)
