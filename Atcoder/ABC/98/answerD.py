#しゃくとり法忘れてた
n=int(input())
a=list(map(int,input().split()))
ans=0
right=0
now=[0]*20#2^20なので
for i in range(n):
    left=i
    if i!=0:
        for j in range(20):
            if (a[left-1]>>j)&1:
                now[j]-=1
    else:
        for j in range(20):
            if (a[left]>>j)&1:
                now[j]+=1
    while all([now[j]<=1 for j in range(20)]):
        #print(100000000)
        right+=1
        if right==n:
            break
        for k in range(20):
            if (a[right]>>k)&1:
                now[k]+=1
    else:
        #print(right)
        for k in range(20):
            if (a[right]>>k)&1:
                now[k]-=1
    right-=1
    ans+=(right-left+1)
    #print(left,right)
print(ans)