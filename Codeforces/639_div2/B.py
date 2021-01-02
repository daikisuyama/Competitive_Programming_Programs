check=[2]
i=0
while check[-1]<=10**9:
    check.append(check[-1]+3*i+5)
    i+=1
print(len(check))
from bisect import bisect_right
def dfs(x):
    if x<2:
        return 0
    return dfs(x-check[bisect_right(check,x)-1])+1
for _ in range(int(input())):
    n=int(input())
    print(dfs(n))