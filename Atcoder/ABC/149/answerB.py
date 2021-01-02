a,b,k=map(int,input().split())
if k<=a:
    print(str(a-k)+" "+str(b))
elif k<=a+b:
    print(str(0)+" "+str(b-(k-a)))
else:
    print("0 0")
