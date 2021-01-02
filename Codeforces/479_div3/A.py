n,k=input().split()
n=[int(i) for i in n]
k=int(k)
for i in range(k):
    if n[-1]==0:
        n=n[:-1]
    else:
        n[-1]-=1
print("".join(map(str,n)))
