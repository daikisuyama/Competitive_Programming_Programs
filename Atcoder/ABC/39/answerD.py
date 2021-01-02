h,w=map(int,input().split())
hw=[["#" for i in range(w+2)] for j in range(h+2)]
for i in range(1,h+1):
    s=input()
    for j in range(1,w+1):
        if s[j-1]==".":
            hw[i][j]="."

def check_8(i,j):
    global h,w
    f1=hw[i-1][j-1]=="#" and hw[i-1][j]=="#" and hw[i-1][j+1]=="#"
    f2=hw[i][j-1]=="#" and hw[i][j]=="#" and hw[i][j+1]=="#"
    f3=hw[i+1][j-1]=="#" and hw[i+1][j]=="#" and hw[i+1][j+1]=="#"
    return f1 and f2 and f3

hw2=[["#" if i==0 or i==w+1 or j==0 or j==h+1 else "." for i in range(w+2)] for j in range(h+2)]


for i in range(1,h+1):
    for j in range(1,w+1):
        if check_8(i,j):
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    hw2[k][l]="#"

if hw!=hw2:
    print("impossible")
else:
    hw3=[["." for i in range(w)] for j in range(h)]
    print("possible")
    for i in range(1,h+1):
        for j in range(1,w+1):
            if check_8(i,j):
                hw3[i-1][j-1]="#"
    for i in range(h):
        print("".join(hw3[i]))

#出力を見ような
#全部checkに含まれるかどうかで判断すれば良い
