n=int(input())
s=input()

if n%2!=0:
    print("No")
elif s[:n//2]!=s[n//2:]:
    print("No")
else:
    print("Yes")
