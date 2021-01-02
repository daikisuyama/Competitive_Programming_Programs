n,m,x,y=map(int,input().split())
X=max(list(map(int,input().split())))
Y=min(list(map(int,input().split())))
print("No War" if any([X<z<=Y for z in range(x+1,y+1)]) else "War")
