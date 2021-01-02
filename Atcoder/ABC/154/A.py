s,t=input().split()
a,b=map(int,input().split())
u=input()
print(str(a)+" "+str(b-1) if u==t else str(a-1)+" "+str(b))