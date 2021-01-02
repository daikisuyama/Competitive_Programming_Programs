n=int(input())
now=[0,0,0]#t,x,y
f=True
for i in range(n):
    t,x,y=map(int,input().split())
    k=abs(x-now[1])+abs(y-now[2])
    l=abs(t-now[0])
    if not(k<=l and abs(k-l)%2==0):
        f=False
    now=[t,x,y]
print("Yes" if f else "No")