a,b,c=map(int,input().split())
x=[]
x.append(a*b*(c-c//2*2))
x.append(b*c*(a-a//2*2))
x.append(c*a*(b-b//2*2))

print(min(x))
