s=input()
x=[0,0,0,0]
for i in s:
    if i=="N":
        x[0]=1
    elif i=="S":
        x[1]=1
    elif i=="W":
        x[2]=1
    else:
        x[3]=1
#print(x)
if x==[1,1,1,1] or x==[0,0,1,1] or x==[1,1,0,0]:
    print("Yes")
else:
    print("No")
