t=int(input())
for i in range(t):
    n=int(input())
    e=sorted(list(map(int,input().split())))
    ans,now=0,0
    while True:
        nowx=now+e[now]
        while nowx<n:
            if nowx-now<e[nowx-1]:
                nowx=now+e[nowx-1]
            else:
                break
        
        if nowx>=n:
            if nowx==n:
                if nowx-now>=e[nowx-1]:
                    ans+=1
            break
        else:
            ans+=1
            now=nowx
    print(ans)