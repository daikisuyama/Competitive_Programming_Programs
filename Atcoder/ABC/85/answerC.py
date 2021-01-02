from sys import exit
n,y=map(int,input().split())
y//=1000
for i in range(y//10+1):
    #k：いくら残ってるか
    #l：何枚使ったか
    k1=y-i*10
    for j in range(k1//5+1):
        k=k1-j*5
        l=i+j
        if k==n-l and i>=0 and j>=0 and k>=0:
            print(str(i)+" "+str(j)+" "+str(k))
            exit()
print("-1 -1 -1")
