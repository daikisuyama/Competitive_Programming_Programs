n,m=map(int,input().split())
x=[[int(j) for j in input().split()][1:] for i in range(n)]
cnt=0
for i in range(1,m+1):
    for j in range(n):
        if i not in x[j]:
            break
    else:
        cnt+=1
print(cnt)
