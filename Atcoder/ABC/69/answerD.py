h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))

hw=[[0 for i in range(w)] for i in range(h)]

k=0#今どこ見ているか
for i in range(h):
    if i%2==0:
        for j in range(w):
            if a[k]==0:
                k+=1
            hw[i][j]=k+1
            a[k]-=1
    else:
        for j in range(w-1,-1,-1):
            if a[k]==0:
                k+=1
            hw[i][j]=k+1
            a[k]-=1
for i in range(h):
    print(" ".join(map(str,hw[i])))
