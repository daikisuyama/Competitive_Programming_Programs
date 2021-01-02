h,w=map(int,input().split())
s=[list(input()) for i in range(h)]
def count_8(i,j):
    global h,w,s
    cnt=0
    if i-1>=0 and j-1>=0:
        if s[i-1][j-1]=="#":
            cnt+=1
    if i-1>=0 and j+1<=w-1:
        if s[i-1][j+1]=="#":
            cnt+=1
    if i+1<=h-1 and j-1>=0:
        if s[i+1][j-1]=="#":
            cnt+=1
    if i+1<=h-1 and j+1<=w-1:
        if s[i+1][j+1]=="#":
            cnt+=1
    if i-1>=0:
        if s[i-1][j]=="#":
            cnt+=1
    if j-1>=0:
        if s[i][j-1]=="#":
            cnt+=1
    if i+1<=h-1:
        if s[i+1][j]=="#":
            cnt+=1
    if j+1<=w-1:
        if s[i][j+1]=="#":
            cnt+=1
    return str(cnt)
for i in range(h):
    for j in range(w):
        if s[i][j]=="#":
            print("#",end="")
        else:
            print(count_8(i,j),end="")
    print()
