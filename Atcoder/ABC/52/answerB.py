n=int(input())
s=input()

ans=[0]
x=0
for i in s:
    if i=="I":
        x+=1
        ans.append(x)
    else:
        x-=1
        ans.append(x)
print(max(ans))
