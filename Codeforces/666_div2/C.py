n=int(input())
a=list(map(int,input().split()))
#first
if n==1:
    print(f"1 1")
    print(f"{-a[0]}")
    print(f"1 1")
    print("0")
    print(f"1 1")
    print("0")
    exit()
if n==2:
    print(f"1 1")
    print(f"{-a[0]}")
    print(f"2 2")
    print(f"{-a[1]}")
    print(f"1 1")
    print("0")
    exit()
print(f"1 {n}")
x=[(n-1-a[i]%(n-1))*n for i in range(n)]
print(" ".join(map(str,x)))
print(f"1 1")
print(f"{-a[0]-x[0]}")
print(f"2 {n}")
print(" ".join(map(str,[-(a[i]+x[i]) for i in range(1,n)])))