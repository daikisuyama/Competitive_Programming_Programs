s=input()
x=""
for i in range(len(s)):
    if s[i]=="1":
        x+="9"
    else:
        x+="1"
print(x)
