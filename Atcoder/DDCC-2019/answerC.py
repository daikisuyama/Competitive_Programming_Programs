h,w,k=map(int,input().split())
x1=[[0 for i in range(w)] for i in range(h)]
x2=[]
x3=[[0 for i in range(w)] for i in range(h)]

for i in range(h):
    s=input()
    l=0
    for j in range(w):
        if s[j]=="#":
            l+=1
            x1[i][j]=1
    x2.append(l)

lx=1
for i in range(h):
    if x2[i]!=0:
        f=0
        for j in range(w):
            if x1[i][j]==1:
                f+=1
                if f==1:
                    x3[i][j]=lx
                else:
                    lx+=1
                    x3[i][j]=lx
                if j==w-1:
                    lx+=1
            else:
                x3[i][j]=lx
                if j==w-1:
                    lx+=1
    else:
        for j in range(w):
            x3[i][j]=-1


for i in range(h):
    if x3[i][0]!=-1:
        print(" ".join(map(str,x3[i])))
    else:
        j=i
        while j<h-1:
            j+=1
            if x3[j][0]!=-1:
                print(" ".join(map(str,x3[j])))
                break
        else:
            j=i
            while True:
                j-=1
                if x3[j][0]!=-1:
                    print(" ".join(map(str,x3[j])))
                    break
