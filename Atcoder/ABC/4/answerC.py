n=int(input())
n%=30
k=n//5
ans=[(k+i+1)%6 if (k+i+1)%6!=0 else 6 for i in range(6)]
l=n%5
#print(ans)
for i in range(l):
    ans[i],ans[i+1]=ans[i+1],ans[i]
for i in range(6):
    print(ans[i],end="")
print()
