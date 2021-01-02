n,a,b,c=map(int,input().split())
s_=input().split()
ans=""
for i in range(n):
    s1,s2=s_[i]
    if s2=="B":
        if i!=n-1:
            if s_[i+1]=="AC" and c==0 and a<=1:
                a,b,ans=(a+1,b-1,ans+"A")
            elif s_[i+1]=="BC" and c==0 and b<=1:
                a,b,ans=(a-1,b+1,ans+"B")
            else:
                a,b,ans=(a-1,b+1,ans+"B") if a>b else (a+1,b-1,ans+"A")
        else:
            a,b,ans=(a-1,b+1,ans+"B") if a>b else (a+1,b-1,ans+"A")
        if min(a,b)==-1:
            print("No")
            break
    elif s1=="A":
        if i!=n-1:
            if s_[i+1]=="AB" and b==0 and a<=1:
                a,c,ans=(a+1,c-1,ans+"A")
            elif s_[i+1]=="BC" and b==0 and c<=1:
                a,c,ans=(a-1,c+1,ans+"C")
            else:
                a,c,ans=(a-1,c+1,ans+"C") if a>c else (a+1,c-1,ans+"A")
        else:
            a,c,ans=(a-1,c+1,ans+"C") if a>c else (a+1,c-1,ans+"A")
        if min(a,c)==-1:
            print("No")
            break
    else:
        if i!=n-1:
            if s_[i+1]=="AB" and a==0 and b<=1:
                b,c,ans=(b+1,c-1,ans+"B")
            elif s_[i+1]=="AC" and a==0 and c<=1:
                b,c,ans=(b-1,c+1,ans+"C")
            else:
                b,c,ans=(b-1,c+1,ans+"C") if b>c else (b+1,c-1,ans+"B")
        else:
            b,c,ans=(b-1,c+1,ans+"C") if b>c else (b+1,c-1,ans+"B")
        if min(b,c)==-1:
            print("No")
            break
else:
    print("Yes")
    for j in range(n):
        print(ans[j])

