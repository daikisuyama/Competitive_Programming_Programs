from collections import *
n,s=input().split()
n=int(n)
x=0
for i in range(n):
  c=Counter()
  for j in range(i,n):
    c[s[j]]+=1
    x+=(c["A"]==c["T"] and c["G"]==c["C"])
print(x)