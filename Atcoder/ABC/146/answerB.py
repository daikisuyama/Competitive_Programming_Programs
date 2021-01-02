c=[chr(i) for i in range(65,65+26)]
#print(c)
n=int(input())
s=input()
for i in range(len(s)):
    if c.index(s[i])+n<26:
        print(c[c.index(s[i])+n],end="")
    else:
        print(c[c.index(s[i])+n-26],end="")
print()
