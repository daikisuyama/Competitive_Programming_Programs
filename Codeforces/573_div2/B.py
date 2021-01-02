ans=2
x=input().split()
for i in ["m","s","p"]:
    c=[int(j[0]) for j in x if j[1]==i]
    c.sort()
    if len(c)<2:
        continue
    if len(c)==3:
        if c[0]==c[1] and c[1]==c[2]:
            ans=0
            break
        if c[0]+1==c[1] and c[1]+1==c[2]:
            ans=0
            break
        if c[0]==c[1] or c[0]+1==c[1] or c[0]+2==c[1]:
            ans=1
            continue
        if c[1]==c[2] or c[1]+1==c[2] or c[1]+2==c[2]:
            ans=1
            continue
    if c[0]==c[1] or c[0]+1==c[1] or c[0]+2==c[1]:
        ans=1
print(ans)