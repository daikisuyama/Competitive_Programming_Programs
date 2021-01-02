k=int(input())
ans=[[i for i in range(1,10)]]
d=9
while d<k:
    ans.append([])
    for i in ans[-2]:
        x=str(i)
        z=int(x[-1])
        ans[-1].append(x+str(z))
        if z<=8:
            ans[-1].append(x+str(z+1))
        if z>=1:
            ans[-1].append(x+str(z-1))
    d+=len(ans[-1])
ans[-1].sort()
print(ans[-1][k-d-1])