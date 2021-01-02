import bisect
n=int(input())
x=[[],[]]
s=input().split()
z=list(map(int,s))
for i in range(3):
    if i==1:
        for j in range(n):
            x_[0].append(int(s[i*n+j]))
        for j in range(n):
            x_[1].append(int(s[i*n+j]))
    elif i==0:
        for j in range(n):
            x_[0].append(int(s[i*n+j]))
    else:
        for j in range(n):
            x_[1].append(int(s[i*n+j]))
x[0].sort()
x[1].sort()
check=[[False]*(2*n),[False]*(2*n)]
for i in range(n):
    k=bisect_left(x[0],z[i])
    while check[0][k]==True:
        k++
    check[0][k]=True
for i in range(n):
    k=bisect_left(x[1],z[-i-1])
    while check[1][k]==True:
        k++
    check[1][k]=True
sum_array=[sum(z[:n]),sum(z[-n:])]
ans_sum=[[],[]]
mi_ma=[0,0]
for j in range(2):
    if j==0:
        for i in range(n):
            if check[j][i]==True:
                mima[j][0]=i
                break
    else:
        for i in range(n-1,-1,-1):
            if check[j][i]==True:
                mima[j][1]=i
#面倒すぎて断念した
