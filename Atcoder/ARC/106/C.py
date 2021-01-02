n,m=map(int,input().split())
if n==1 and m==0:
    print(1,2)
    exit()
if m==n or m==n-1 or m<0:
    print(-1)
    exit()
ans=[[1,10**7]]
for i in range(m+1):
    ans.append([2*(i+1),2*(i+1)+1])
for i in range(n-m-2):
    ans.append([10**7+2*(i+1),10**7+2*(i+1)+1])
#print(ans)
for i in ans:
    print(i[0],i[1])