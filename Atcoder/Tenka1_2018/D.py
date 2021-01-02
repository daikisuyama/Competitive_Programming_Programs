n=int(input())
n*=2
def make_divisors():
    divisors=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            divisors.append(i)
            if i!=n//i:
                divisors.append(n//i)
    return divisors
for i in make_divisors():
    if i+1==n//i:
        print("Yes")
        print(i+1)
        ans=[[0]*i for j in range(i+1)]
        s=1
        for j in range(i):
            #print(j)
            ans[j][j]=s
            for k in range(i-j):
                ans[j+1+k][j]=s+k
                ans[j][j+k]=s+k
            s+=(i-j)
        for j in range(i+1):
            print(" ".join(map(str,[i]+ans[j])))
        break
else:
    print("No")