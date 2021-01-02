n=int(input())
now=input()
s=set()
s.add(now)
for i in range(n-1):
    now2=input()
    if now[-1]!=now2[0]:
        print("No")
        break
    now=now2
    s.add(now)
else:
    if len(s)==n:
        print("Yes")
    else:
        print("No")