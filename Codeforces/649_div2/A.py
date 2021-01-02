for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    if all([i%x==0 for i in a]):
        print(-1)
    else:
        if sum(a)%x!=0:
            print(n)
        else:
            #%xが0以外出るまで
            l,r=0,0
            for i in range(n):
                if a[i]%x!=0:
                    l=i
                    break
            for i in range(n):
                if a[n-i-1]%x!=0:
                    r=i
                    break
            print(n-min(l,r)-1)