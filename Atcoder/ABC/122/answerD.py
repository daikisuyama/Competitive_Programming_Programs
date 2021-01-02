n=int(input())
alph=["A","C","G","T"]
a=[alph[i]+alph[j]+alph[k] for i in range(4) for j in range(4) for k in range(4)]
d1={l:0 for l in a}
for i in d1:
    if i!="AGC" and i!="ACG" and i!="GAC":
        d1[i]=1
d2={l:0 for l in a}
for i in range(n-3):
    for j in d1:
        next=[j+alph[k] for k in range(4)]
        for k in range(4):
            l=next[k]
            if l[1:]=="GAC" or l[1:]=="ACG" or l[1:]=="AGC":
                pass
            elif l[0]=="A" and l[3]=="C" and (l[1]=="G" or l[2]=="G"):
                pass
            else:
                d2[l[1:]]+=d1[j]
    for j in d1:
        d1[j]=d2[j]
        d2[j]=0
print(sum(d1.values())%(1000000007))