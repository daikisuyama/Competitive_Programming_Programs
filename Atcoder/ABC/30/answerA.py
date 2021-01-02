a,b,c,d=map(int,input().split())
eps=1/1000000000
if abs(b/a-d/c)<eps:
    print("DRAW")
elif b/a-d/c>0:
    print("TAKAHASHI")
else:
    print("AOKI")
