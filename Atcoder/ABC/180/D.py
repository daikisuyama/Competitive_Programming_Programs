x,y,a,b=map(int,input().split())
ans=0
while True:
    if x*a<=x+b:
        if x*a>=y:
            print(ans)
            exit()
        else:
            ans+=1
            x*=a
    else:
        #こっから+
        #x*a>x+b
        #x<y
        break
print(ans+(y-x-1)//b)