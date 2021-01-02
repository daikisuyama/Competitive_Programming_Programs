n=int(input())
check=[[0]*9 for i in range(9)]
for i in range(1,n+1):
    s=str(i)
    s1=int(s[0])-1
    s2=int(s[-1])-1
    if s2==-1:continue
    check[s1][s2]+=1
cnt=0
for i in range(9):
    for j in range(9):
        cnt+=check[i][j]*check[j][i]
print(cnt)
