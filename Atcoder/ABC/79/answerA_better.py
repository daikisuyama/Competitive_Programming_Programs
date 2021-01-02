n=input()
x=[int(i) for i in n]
print("Yes" if x[1]==x[2] and (x[0]==x[1] or x[2]==x[3]) else "No")
