N=input()
A1=input().split()
B1=input().split()
A2,B2=[],[]
for i in A1:
    A2.append(int(i))
for i in B1:
    B2.append(int(i))

s=0
for i in range(len(B2)):
    if A2[i]==0 or B2[i]==0:
        pass
    elif A2[i] >= B2[i]:
        s+=B2[i]
        A2[i]-=B2[i]
        B2[i]=0
    else:
        s+=A2[i]
        B2[i]-=A2[i]
        A2[i]=0

    if A2[i+1]==0 or B2[i]==0:
        continue
    elif A2[i+1] >= B2[i]:
        s+=B2[i]
        A2[i+1]-=B2[i]
        B2[i]=0
    else:
        s+=A2[i+1]
        B2[i]-=A2[i+1]
        A2[i+1]=0

print(s)
