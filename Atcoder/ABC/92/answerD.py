a,b=map(int,input().split())
print("100 100")
a-=1
b-=1
for i in range(100):
    if i%2==0:
        print("."*50+"#"*50)
    else:
        for j in range(50):
            if j%2==0 or j==49:
                print(".",end="")
            else:
                if b>0:
                    print("#",end="")
                    b-=1
                else:
                    print(".",end="")
        for j in range(50):
            if j%2==0 or j==49:
                print("#",end="")
            else:
                if a>0:
                    print(".",end="")
                    a-=1
                else:
                    print("#",end="")
        print("")
