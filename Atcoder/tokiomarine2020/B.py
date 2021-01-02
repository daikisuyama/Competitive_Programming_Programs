a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())
if a<b and v<=w:
    print("NO")
elif a>b and v<=w:
    print("NO")
elif a<b:
    if -((a-b)//(v-w))<=t:
        print("YES")
    else:
        print("NO")
else:
    if -((-a+b)//(v-w))<=t:
        print("YES")
    else:
        print("NO")