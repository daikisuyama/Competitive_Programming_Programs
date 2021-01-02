h,w,n=map(int,input().split())
d=dict()
def change(a,b):
    global h,w,d
    if 1<=a<h-1 and 1<=b<w-1:
        if (a,b) in d:
            d[(a,b)]+=1
        else:
            d[(a,b)]=1
for i in range(n):
    a,b=map(int,input().split())
    a-=1
    b-=1
    for j in range(3):
        for k in range(3):
            change(a+j-1,b+k-1)
ans=[0]*10
ans[0]=(h-2)*(w-2)

for i in d:
    ans[d[i]]+=1
    ans[0]-=1
for i in range(10):
    print(ans[i])

