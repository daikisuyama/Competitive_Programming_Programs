n=int(input())
mnm=""
mnu=0
sm=0
for i in range(n):
    s,p=input().split()
    sm+=int(p)
    if mnu<int(p):
        mnu=int(p)
        mnm=s

if sm//2 < mnu:
    print(mnm)
else:
    print("atcoder")
