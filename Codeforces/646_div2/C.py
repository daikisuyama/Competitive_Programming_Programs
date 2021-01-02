name=["Ayush","Ashish"]
for _ in range(int(input())):
    n,x=map(int,input().split())
    check=0
    for i in range(n-1):
        u,v=map(int,input().split())
        if u==x or v==x:
            check+=1
    if check==0 or check==1:
        print(name[0])
    else:
        print(name[n%2])