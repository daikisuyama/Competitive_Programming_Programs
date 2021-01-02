s=input()
t=s.split("+")
c=0
for i in t:
    if "0" not in i:
        c+=1
print(c)
