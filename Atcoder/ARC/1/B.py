a,b=map(int,input().split())
ans=abs(b-a)
for i in range(-5,6):
  for j in range(-9,10):
    for k in range(-41,42):
      if 10*i+5*j+k==b-a:
        ans=min(sum(map(abs,[i,j,k])),ans)
print(ans)