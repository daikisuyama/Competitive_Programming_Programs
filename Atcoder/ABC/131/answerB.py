N,L=input().split()
N,L=int(N),int(L)
k=N*(2*L+N-1)//2
if L >=0:
    print(k-L)
elif L+N-1 <=0:
    print(k-L-N+1)
else:
    print(k)
