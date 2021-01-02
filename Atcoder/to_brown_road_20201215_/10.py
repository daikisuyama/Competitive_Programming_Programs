a,b=map(int,input().split())
s=input()
if s[a]!="-":
    print("No")
else:
    s=s[:a]+s[a+1:]
    print(["No","Yes"][s.isdecimal()])