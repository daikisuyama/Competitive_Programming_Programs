n,z=map(int,input().split())
for x in range(1,z):
    y=int((z**n-x**n)**(1/n))
    if x**n+y**n==z**n:
        print("Yes")
        break
else:
    print("No")
