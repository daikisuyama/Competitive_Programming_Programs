s=input()
n=len(s)
for i in range(n):
    if i%2==0 and s[i]!="h":
        print("No")
        break
    if i%2!=0 and s[i]!="i":
        print("No")
        break
else:
    if n%2==0:
        print("Yes")
    else:
        print("No")