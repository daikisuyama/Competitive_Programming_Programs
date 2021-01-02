N=int(input())
s=[]
n=[]
for i in range(N):
    k="".join(sorted(list(input())))
    if k in s:
        n[s.index(k)]+=1
    else:
        s.append(k)
        n.append(1)
c=0
for i in n:
    c += i*(i-1)

print(c//2)
