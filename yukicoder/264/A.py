t="abcdefghijklmnopqrstuvwxyz"
s=input()
for i in range(26):
    if s[i]!=t[i]:
        print(t[i]+"to"+s[i])
        break