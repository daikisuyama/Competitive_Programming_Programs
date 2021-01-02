#一次独立：rankが成分数
import numpy as np
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=input()
    matrix=np.zeros((60,1))
    for i in range(n-1,-1,-1):
        ne=np.array([(a[i]>>j)&1 for j in range(60)])
        matrix=np.c_[matrix,ne]
        col=matrix.shape[1]
        ra=np.linalg.matrix_rank(matrix)
        if s[i]=="0":
            if col!=ra+1:
                matrix=np.delete(matrix,col-1,1)
        else:
            if col==ra+1:
                print(1)
                break
    else:
        print(0)