x=int(input())
h=[1800,1600,1400,1200,1000,800,600,400]
for i in range(8):
    if x>=h[i]:
        print(i+1)
        break