n=int(input())
r=list(map(int,input().split()))
if n<3:
    print(0)
    exit()
ans=[r[0]]
for i in range(1,n-1):
    if ans[-1]<r[i] and r[i]>r[i+1]:
        ans.append(r[i])
    if ans[-1]>r[i] and r[i]<r[i+1]:
        ans.append(r[i])
    if i==n-2:
        ans.append(r[i+1])
if len(ans)<3:
    print(0)
else:
    print(len(ans))