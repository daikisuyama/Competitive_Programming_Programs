N,D=input().split()
N,D=int(N),int(D)

k=N//(2*D+1)
if N%(2*D+1) == 0:
    print(k)
else:
    print(k+1)
