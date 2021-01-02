s=input()
l=len(s)
t=input()
k=len(t)
cand=[]
for i in range(l-k+1):
    new=""
    for j in range(l):
        if i<=j<i+k:
            if s[j]=="?":
                new+=t[j-i]
            else:
                if s[j]==t[j-i]:
                    new+=t[j-i]
                else:
                    break
        else:
            if s[j]=="?":
                new+="a"
            else:
                new+=s[j]
    if len(new)==l:
        cand.append(new)
cand.sort()
if len(cand)==0:
    print("UNRESTORABLE")
else:
    print(cand[0])