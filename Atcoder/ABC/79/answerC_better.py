a,b,c,d=[int(i) for i in input()]

if a+b+c+d==7:
    print("{}+{}+{}+{}=7".format(a,b,c,d))
elif a+b+c-d==7:
    print("{}+{}+{}-{}=7".format(a,b,c,d))
elif a+b-c+d==7:
    print("{}+{}-{}+{}=7".format(a,b,c,d))
elif a-b+c+d==7:
    print("{}-{}+{}+{}=7".format(a,b,c,d))
elif a+b-c-d==7:
    print("{}+{}-{}-{}=7".format(a,b,c,d))
elif a-b+c-d==7:
    print("{}-{}+{}-{}=7".format(a,b,c,d))
elif a-b-c+d==7:
    print("{}-{}-{}+{}=7".format(a,b,c,d))
else:
    print("{}-{}-{}-{}=7".format(a,b,c,d))
