n=int(input())
#nが小さい場合
for i in range(n-1):
    x=[str(j+1) for j in range(n-i-1)]
    print(" ".join(x))
