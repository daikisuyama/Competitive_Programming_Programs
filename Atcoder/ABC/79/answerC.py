a,b,c,d=[int(i) for i in input()]
l=7-a
f=[-1,-1,-1]
for i in range(2):
    for j in range(2):
        for k in range(2):
            l_sub=l
            if i==0:
                l_sub-=(b)
            else:
                l_sub-=(-b)
            if j==0:
                l_sub-=(c)
            else:
                l_sub-=(-c)
            if k==0:
                l_sub-=(d)
            else:
                l_sub-=(-d)
            if l_sub==0:
                f=[i,j,k]
        if f!=[-1,-1,-1]:
            break
    if f!=[-1,-1,-1]:
        break
s=str(a)
if f[0]==0:
    s+="+"
else:
    s+="-"
s+=str(b)
if f[1]==0:
    s+="+"
else:
    s+="-"
s+=str(c)
if f[2]==0:
    s+="+"
else:
    s+="-"
s+=str(d)
s+="=7"

print(s)
