x=[1,3,5,7,8,10,12]
y=[4,6,9,11]
z=[2]

a,b=map(int,input().split())

if (a in x and b in x) or (a in y and b in y) or (a in z and b in z):
    print("Yes")
else:
    print("No")
