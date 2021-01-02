h,w=map(int,input().split())
s=[list(input()) for i in range(h)]
t=[["" for j in range(h)] for i in range(w)]
for i in range(h):
    for j in range(w):
        t[j][i]=s[i][j]
ans=0
for i in range(h):
    for j in range(w-1):
        if s[i][j]=="." and s[i][j+1]==".":
            ans+=1
for i in range(w):
    for j in range(h-1):
        if t[i][j]=="." and t[i][j+1]==".":
            ans+=1
print(ans)