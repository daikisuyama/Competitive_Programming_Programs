n,k=map(int,input().split())
s=input()
if s[k-1]=="A":
    print(s[:k-1]+"a"+s[k:])
elif s[k-1]=="B":
    print(s[:k-1]+"b"+s[k:])
else:
    print(s[:k-1]+"c"+s[k:])