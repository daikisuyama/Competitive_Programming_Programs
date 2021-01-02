for _ in range(int(input())):
    x1,y1,x2,y2=map(int,input().split())
    a,b=(x2-x1+1),(y2-y1+1)
    if a>b:
        a,b=b,a
    print((a-2)*(a-1)+(a-1)+(a-1)*(b-a)+1)