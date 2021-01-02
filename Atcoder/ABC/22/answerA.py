n,s,t=map(int,input().split())

w=int(input())
c=0
if s<=w<=t:
    c+=1
for i in range(n-1):
    w+=int(input())
    if s<=w<=t:
        c+=1
    #print(w)
print(c)
