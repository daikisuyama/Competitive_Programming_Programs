ans=0
x,y=map(int,input().split())
print(max(4-x,0)*100000+max(4-y,0)*100000+(x==1 and y==1)*400000)