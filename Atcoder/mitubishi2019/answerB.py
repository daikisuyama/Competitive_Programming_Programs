x=[]
for i in range(1,50001):
    x.append(int(i*1.08))

n=int(input())
for i in range(50000):
    if n==x[i]:
        print(i+1)
        break
else:
    print(":(")
