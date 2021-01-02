n,q=map(int,input().split())
a=list(map(int,input().split()))
check=[[0,0] for i in range(32)]
s=list(map(int,input()))
for i in range(32):
    #初期状態が0か1か
    for k in range(2):
        x=k
        for j in range(n):
            if (a[j]>>i)&1:
                if s[j]==0:
                    if x==0:
                        check[i][k]+=0
                        x=0
                    else:
                        check[i][k]+=0
                        x=1
                else:
                    if x==0:
                        check[i][k]+=1
                        x=1
                    else:
                        check[i][k]+=0
                        x=1
            else:
                if s[j]==0:
                    if x==0:
                        check[i][k]+=0
                        x=0
                    else:
                        check[i][k]+=1
                        x=0
                else:
                    if x==0:
                        check[i][k]+=0
                        x=0
                    else:
                        check[i][k]+=0
                        x=1
#print(check)
t=list(map(int,input().split()))
for _ in range(q):
    z=t[_]
    ans=0
    for i in range(32):
        ans+=(check[i][(z>>i)&1]*(2**i))
        #print(ans)
    print(ans)