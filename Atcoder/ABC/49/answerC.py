s=input()
l=len(s)
while s!=0:
    l=len(s)
    if s.rfind("dream")==l-5:
        s=s[:l-5]
    elif s.rfind("dreamer")==l-7:
        s=s[:l-7]
    elif s.rfind("erase")==l-5:
        s=s[:l-5]
    elif s.rfind("eraser")==l-6:
        s=s[:l-6]
    else:
        break
if len(s)==0:
    print("YES")
else:
    print("NO")
    