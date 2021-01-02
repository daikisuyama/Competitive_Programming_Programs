n=int(input())
k=n%111
if k==0:
    print(n)
else:
    print(n-k+111)
