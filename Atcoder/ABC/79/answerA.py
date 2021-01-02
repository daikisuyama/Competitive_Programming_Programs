n=input()
x=[int(i) for i in n]

if (x[0]==x[1] and x[1]==x[2]) or (x[1]==x[2] and x[2]==x[3]):
    print("Yes")
else:
    print("No")
