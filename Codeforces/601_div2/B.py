n=int(input())
a=list(map(int,input().split()))
#すでに来た人
s=set()
#今解消しなければならない人
b=set()
#どの日までみたか
now=0
#答えの配列
ans=[]
while now<n:
    if a[now]>0:
        if a[now] in s:
            print(-1)
            exit()
        else:
            s.add(a[now])
            b.add(a[now])
    else:
        if -a[now] not in b:
            print(-1)
            exit()
        else:
            b.remove(-a[now])
    if len(b)==0:
        ans.append(now+1)
        s=set()
    now+=1
if len(b)!=0:
    print(-1)
    exit()
for i in range(len(ans)-1,0,-1):
    ans[i]-=ans[i-1]
print(len(ans))
print(" ".join(map(str,ans)))
