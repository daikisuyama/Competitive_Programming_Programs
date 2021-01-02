m=int(input())

if m<100:
    print("00")
elif m<=5000:
    k=(m*10)//1000
    if k<10:
        print("0"+str(k))
    else:
        print(k)
elif m<=30000:
    print(m//1000+50)
elif m<=70000:
    print((m//1000-30)//5+80)
else:
    print(89)
