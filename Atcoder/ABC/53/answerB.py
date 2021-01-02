s=input()
n=len(s)
a,b=0,0
for i in range(n):
    if s[i]=="A":
        a=i
        break
for i in range(n-1,-1,-1):
    if s[i]=="Z":
        b=i
        break
print(b-a+1)
