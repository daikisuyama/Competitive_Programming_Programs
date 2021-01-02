a,b=map(int,input().split())
if a==1 or b==1:
    print("Alice" if a==1 else "Bob" if b==1 else "Draw")
else:
    print("Alice" if a>b else "Bob" if a<b else "Draw")
