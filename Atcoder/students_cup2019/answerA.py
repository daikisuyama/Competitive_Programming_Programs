m,d=input().split()
m,d=int(m),int(d)

c=0
if d<22:
    print(0)
else:
    for j in range(m):
        for i in range(d-21):
            d1,d10=int(str(i+22)[1]),int(str(i+22)[0])
            #print(d1)
            #print(d10)
            if d1>1 and d10>1 and d1*d10==j+1:
                c+=1
                #print(j+1,i+22)
    print(c)
