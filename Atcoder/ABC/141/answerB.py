s=input()
c=0
for i in range(len(s)):
    if i%2==0 and s[i] in ["R","U","D"]:
        c+=1
    if i%2==1 and s[i] in ["L","U","D"]:
        c+=1
if c==len(s):
    print("Yes")
else:
    print("No")
