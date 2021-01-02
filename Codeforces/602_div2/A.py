for _ in range(int(input())):
    n=int(input())
    lr=[]
    for i in range(n):
        x,y=map(int,input().split())
        lr.append([x,y])
    lr.sort(key=lambda x:x[1])
    ab=[lr[0][1],lr[0][1]]
    for i in range(1,n):
        if ab[1]<lr[i][0]:
            ab[1]=lr[i][0]
    print(ab[1]-ab[0])