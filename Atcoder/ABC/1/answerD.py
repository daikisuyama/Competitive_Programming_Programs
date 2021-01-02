def ro(z):y=(int(z[1])-1)//5*5+5;return [int(z[0])//5*5,y+(y%100==60)*40]
n=int(input())
se=sorted([ro(input().split("-"))for i in[0]*n])
ans=[se[0]]
for i in range(1,n):
    if se[i][0]<=ans[-1][1]:ans[-1][1]=max(ans[-1][1],se[i][1])
    else:ans.append(se[i])
for i in ans:print("-".join(map(lambda x:str(x).zfill(4),i)))