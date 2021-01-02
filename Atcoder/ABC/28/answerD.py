n,k=map(int,input().split())
A=n*n*n
B=6*(k-1)*(n-k)
B+=1
B+=3*(k-1)
B+=3*(n-k)
print(B/A)
#ただの確率
