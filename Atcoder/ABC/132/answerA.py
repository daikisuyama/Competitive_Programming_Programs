S1=input()
S2={}
for i in range(4):
    if S1[i] in S2:
        S2[S1[i]]+=1
    else:
        S2[S1[i]]=1
if len(S2)==2 and S2[S1[0]]==2:
    print("Yes")
else:
    print("No")
