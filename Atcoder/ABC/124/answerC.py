s=input()
l=len(s)
sa=""
sb=""
for i in range(l):
    if i%2==0:
        sa+="0"
        sb+="1"
    else:
        sa+="1"
        sb+="0"
ca=0
cb=0
for i in range(l):
    if sa[i]!=s[i]:
        ca+=1
    if sb[i]!=s[i]:
        cb+=1
#print(ca)
#print(cb)
print(min(ca,cb))
