s=input()
#print(s[1]+s[2:2+s[2:-1].index("C")]+s[s[2:-1].index("C")+1:])
if s[0]=="A" and s[2:-1].count("C")==1:
    if (s[1]+s[2:2+s[2:-1].index("C")]+s[s[2:-1].index("C")+3:]).islower():
        print("AC")
    else:
        print("WA")
else:
    print("WA")