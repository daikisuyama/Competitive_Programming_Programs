n=int(input())
s=input()
if s[0]=="(":
    c=1
    d=1
else:
    c=-1
    d=-1
for i in range(1,n):
    if s[i]=="(":
        d+=1
    else:
        d-=1
        c=min(c,d)
if c<0:
    s="("*(-c)+s
print(s+")"*(s.count("(")-s.count(")")))
