s=input()
n=len(s)
if s[0]==s[-1]:
    if n%2==0:
        print("First")
    else:
        print("Second")
elif s[0]!=s[-1]:
    if n%2==1:
        print("First")
    else:
        print("Second")