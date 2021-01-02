I=input
n=int
for i in range(n(input())):
  I();t=[];x=0
  for i,j in zip(map(n,I().split()[::-1]),I()[::-1]):
    [i:=(i^k*(i^k<i))for k in t];j=n(j);t+=[i*(j^1)];x|=(i>0)&j
  print(x)