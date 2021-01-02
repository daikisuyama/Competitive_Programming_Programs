n,k=map(int,input().split())
s=input()
t=[[s,(2**k)//n],s[:(2**k)%n]]
#print(t)
for i in range(k):
    if len(t[0][0])%2==1:
        if t[0][1]%2==1:
            t[1]=t[0][0]+t[1]
            t[0][1]//=2
            t[0][0]=2*t[0][0]
        else:
            t[0][1]//=2
            t[0][0]=2*t[0][0]
    l=len(t[0][0])
    nt=""
    for i in range(l//2):
        if t[0][0][2*i]=="R":
            if t[0][0][2*i+1]=="P":
                nt+="P"
            else:
                nt+="R"
        elif t[0][0][2*i]=="S":
            if t[0][0][2*i+1]=="R":
                nt+="R"
            else:
                nt+="S"
        else:
            if t[0][0][2*i+1]=="S":
                nt+="S"
            else:
                nt+="P"
        #print(nt)
    t[0][0]=nt
    l=len(t[1])
    nt=""
    for i in range(l//2):
        if t[1][2*i]=="R":
            if t[1][2*i+1]=="P":
                nt+="P"
            else:
                nt+="R"
        elif t[1][2*i]=="S":
            if t[1][2*i+1]=="R":
                nt+="R"
            else:
                nt+="S"
        else:
            if t[1][2*i+1]=="S":
                nt+="S"
            else:
                nt+="P"
        #print(nt)
    t[1]=nt
    #print(t)
if t[1]=="":
    print(t[0][0])
else:
    print(t[1])