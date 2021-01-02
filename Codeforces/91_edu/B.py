t=int(input())
for i in range(t):
    S=input()
    l=len(S)
    r=S.count("R")
    s=S.count("S")
    p=S.count("P")
    m=max(r,s,p)
    if m==r:
        print("P"*l)
    elif m==s:
        print("R"*l)
    else:
        print("S"*l)