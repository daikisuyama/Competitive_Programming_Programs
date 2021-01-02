x=[chr(i) for i in range(97, 97+26)]
y=[0]*26
s=input()
for i in s:
    y[x.index(i)]=1
for i in range(26):
    if y[i]==0:
        print(chr(97+i))
        break
else:
    print("None")
