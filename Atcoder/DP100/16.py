import numpy as np
import numba
@numba.jit
def solve(n,s):
    dp=np.zeros((n+1,n+1),dtype=np.int16)
    for i in range(n):
        for j in range(i+1,n):
            if s[i]==s[j]:
                if dp[i][j]<j-i:
                    dp[i+1][j+1]=dp[i][j]+1
    print(np.amax(dp))
n=int(input())
s=np.array([ord(i) for i in input()])
solve(n,s)