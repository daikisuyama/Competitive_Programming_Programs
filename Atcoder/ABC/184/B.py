n,x=map(int,input().split())
s=input()
for i in range(n):
    if s[i]=="o":
        x+=1
    else:
        x-=1
        x=max(x,0)
print(x)