x=input()
while True:
    if len(x)==0:
        print("YES")
        break
    elif x[-1]=="o" or x[-1]=="k" or  x[-1]=="u":
        x=x[:-1]
    elif len(x)==1:#これ忘れると、次が多分REになる
        print("NO")
        break
    elif x[-2:]=="ch":
        x=x[:-2]
    else:
        print("NO")
        break
