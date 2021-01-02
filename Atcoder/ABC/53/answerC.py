x=int(input())
ans=0
ans+=(x//11)*2
x-=(x//11)*11
if x==0:
    print(ans)
elif x<=6:
    print(ans+1)
else:
    print(ans+2)
