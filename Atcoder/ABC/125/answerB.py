n=int(input())
v=input().split()
c=input().split()
co=0
for i in range(n):
    co+=max(0,int(v[i])-int(c[i]))
print(co)
