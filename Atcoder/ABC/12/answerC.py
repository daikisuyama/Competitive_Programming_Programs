x=(1+2+3+4+5+6+7+8+9)*(1+2+3+4+5+6+7+8+9)
k=x-int(input())
ans=[]
for i in range(1,10):
    if k%i==0 and 1<=k//i<=9:
        ans.append("{} x {}".format(i,k//i))
for i in ans:
    print(i)
