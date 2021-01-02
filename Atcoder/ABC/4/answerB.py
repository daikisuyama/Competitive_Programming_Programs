d=[[i for i in input().split()][::-1] for j in range(4)]
for i in range(4):
    print(" ".join(d[4-i-1]))
