cand=[60*i*60//11 for i in range(12)]
#print(cand)
a,b=map(int,input().split())
a%=12
b*=60
#print(int(cand[a]-b),int(cand[a]+360-b))
if cand[a]>=b:
    print(int(cand[a]-b))
else:
    a=(a+1)%12
    print(int(cand[a]+3600-b))