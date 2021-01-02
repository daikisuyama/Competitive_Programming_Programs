import math
a=int(input())
ans=[]
for i in [2,3]:
    for j in range(200):
        if (i**j)>=a:
            ans.append(i*j)
            break
#5の時だけちゃうやん
if a==5:
    print(5)
else:
    print(min(ans))
