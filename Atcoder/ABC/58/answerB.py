o=input()
lo=len(o)
e=input()
le=len(e)
for i in range(lo+le):
    if i%2==0:
        print(o[i//2],end="")
    else:
        print(e[i//2],end="")
print()
