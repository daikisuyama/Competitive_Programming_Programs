a=int(input())
b=int(input())
c=int(input())
x=[a,b,c]
y=[]
for i in range(3):
    if x[i]==max(x):
        y.append(1)
    elif x[i]==min(x):
        y.append(3)
    else:
        y.append(2)
for i in range(3):
    print(y[i])
