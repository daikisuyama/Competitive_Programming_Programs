s=input()
l=len(s)

c=0
for i in range(l//2):
    if s[i]!=s[-i-1]:
        c+=1
print(c)
