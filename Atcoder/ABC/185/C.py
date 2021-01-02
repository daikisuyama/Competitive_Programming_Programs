ans=1
l=int(input())
for i in range(11):
    ans*=(l-1-i)
for i in range(11):
    ans//=(i+1)
print(ans)