h,w=map(int,input().split())
s=[input()+"." if i!=h else "."*(w+1) for i in range(h+1)]
def count_8(i,j):
    global h,w,s
    cnt=(s[i-1][j-1]=="#")+(s[i-1][j+1]=="#")+(s[i+1][j-1]=="#")+(s[i+1][j+1]=="#") \
        +(s[i-1][j]=="#")+(s[i][j-1]=="#")+(s[i+1][j]=="#")+(s[i][j+1]=="#")
    return cnt
for i in range(h):
    s_sub=""
    for j in range(w):
        if s[i][j]=="#":
            s_sub+="#"
        else:
            s_sub+=str(count_8(i,j))
    print(s_sub)