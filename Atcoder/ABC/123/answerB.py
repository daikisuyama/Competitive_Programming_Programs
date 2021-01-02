import math
x=[int(input()) for i in range(5)]
y=[i%10 for i in x]
ans=0
for i in range(5):
    ans+=math.ceil(x[i]/10)*10
check=10
for i in range(5):
    if y[i]!=0:
        check=min(check,y[i])
if check==10:
    print(ans)
else:
    print(ans-(10-check))
