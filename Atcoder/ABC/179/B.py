n=int(input())
x,y=[],[]
for i in range(n):
    x_,y_=map(int,input().split())
    x.append(x_)
    y.append(y_)
for i in range(n-2):
    if x[i]==y[i] and x[i+1]==y[i+1] and x[i+2]==y[i+2]:
        print("Yes")
        break
else:
    print("No")