n=int(input())
x3,x5=[3],[5]
while True:
    if x3[-1]*3<n:
        x3.append(x3[-1]*3)
    else:
        break
while True:
    if x5[-1]*5<n:
        x5.append(x5[-1]*5)
    else:
        break
x3,x5=[i for i in x3 if i<n],[i for i in x5 if i<n]
y3,y5=set(x3),set(x5)
#print(y3,y5)
for i in y3:
    if n-i in y5:
        a,b=i,n-i
        ans1,ans2=0,0
        while a!=1:
            a//=3
            ans1+=1
        while b!=1:
            b//=5
            ans2+=1
        print(ans1,ans2)
        exit()
print(-1)