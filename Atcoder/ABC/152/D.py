n=int(input())
check1=[[i,i,0] for i in range(1,10)]
check2=[[i,j,0] for i in range(1,10) for j in range(i+1,10)]
l=len(check2)
check3=[[check2[i][1],check2[i][0],0] for i in range(l)]

for i in range(1,n+1):
    s=str(i)
    s1=int(s[0])
    s2=int(s[-1])
    if s2!=0:
        if s1==s2:
            check1[s1-1][2]+=1
        elif s1<s2:
            x=[0,8,15,21,26,30,33,35]
            check2[x[s1-1]+(s2-s1-1)][2]+=1
        else:
            x=[0,8,15,21,26,30,33,35]
            check3[x[s2-1]+(s1-s2-1)][2]+=1
cnt=0
for i in range(9):
    cnt+=(check1[i][2])*(check1[i][2])
for i in range(l):
    cnt+=2*(check2[i][2]*check3[i][2])
print(cnt)
