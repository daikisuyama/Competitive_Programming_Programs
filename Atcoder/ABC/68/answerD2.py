k=int(input())
n=k+1
if n==1:
    print("2")
    print("0 1")
else:
    print(n-1+k*n,end="")
    for i in range(n-1):
        print(" 0",end="")
    print()
