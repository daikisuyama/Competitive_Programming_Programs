n=int(input())
k=n
f=0
while k!=0:
    f+=(k%10)
    k//=10
print("Yes" if n%f==0 else "No")