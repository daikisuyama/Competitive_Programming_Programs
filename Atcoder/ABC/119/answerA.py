s=input()

s=s[5:7]

if s[0]=="0":
    s=int(s[1])
    if s>4:
        print("TBD")
    else:
        print("Heisei")
else:
    print("TBD")
