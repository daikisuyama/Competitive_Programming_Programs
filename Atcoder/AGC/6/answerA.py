n=int(input())
s=input()
t=input()

if s==t:
    print(n)
else:
    for i in range(n):
        u=s[:i+1]+t
        if u[:n]==s:
            print(n+i+1)
            break
