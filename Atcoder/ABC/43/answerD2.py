from sys import exit
s=input()
l=len(s)
for i in range(l-2):
    if s[i]==s[i+2]:
        print(str(i+1)+" "+str(i+3))
        exit()
    if s[i]==s[i+1]:
        print(str(i+1)+" "+str(i+2))
        exit()
if s[l-2]==s[l-1]:
    print(str(l-1)+" "+str(l))
else:
    print("-1 -1")
