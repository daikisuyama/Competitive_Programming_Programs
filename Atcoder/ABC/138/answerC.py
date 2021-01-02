n=int(input())
v=sorted([int(i) for i in input().split()])
#y=(v[0]+v[1])/2
z=v[0]
for i in range(n-1):
    z=(z+v[i+1])/2

print(z)
