a,b=map(int,input().split())
for i in range(1,1000000):
    if (i*2)//25==a and i//10==b:
        print(i)
        break
else:
    print(-1)