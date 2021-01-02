a,b,x,y=map(int,input().split())
if a==b:
    print(x)
elif b<a:
    #斜めに降りる
    ans=x
    c=abs(a-b)-1
    #cを0にする
    print(ans+min(2*x*c,y*c))
else:
    ans=x
    c=abs(a-b)
    print(ans+min(2*x*c,y*c))