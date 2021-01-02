s=input()
t=input()
at=["a","t","c","o","d","e","r","@"]
for i in range(len(s)):
    if s[i]==t[i] or (s[i]=="@" and t[i] in at) or (t[i]=="@" and s[i] in at):
        pass
    else:
        print("You will lose")
        break
else:
    print("You can win")
