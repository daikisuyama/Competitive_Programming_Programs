n=int(input())
s=input()
ans=[]
if n%2==1:
    ans.append(s[0])
    s=s[1:]
    n-=1
a,b=[],[]
for i in range(n//2):
    a.append(s[2*i])
    b.append(s[2*i+1])
print("".join(a[::-1]+ans+b))
