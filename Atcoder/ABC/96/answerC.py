h,w=map(int,input().split())
s=[input() for i in range(h)]

#四つのうち#があればOK
def four_next(i,j):
    global s
    if i>0 :
        if s[i-1][j]=="#":
            return True
    if i<h-1 :
        if s[i+1][j]=="#":
            return True
    if j>0 :
        if s[i][j-1]=="#":
            return True
    if j<w-1 :
        if s[i][j+1]=="#":
            return True
    return False

f=0
for i in range(h):
    for j in range(w):
        if s[i][j]=="#" and (not four_next(i,j)):
            f=1
            break
    if f==1:
        break
if f==0:
    print("Yes")
else:
    print("No")
