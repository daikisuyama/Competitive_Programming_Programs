n=int(input())
l=sorted([int(i) for i in input().split()],reverse=True)

#print(l)
co=0
for i in range(n-2):
    c=l[i]
    x=0
    for j in range(i+1,n-1):
        b=l[j]
        for k in range(j+1,n):
            a=l[k]
            if c<(a+b):
                co+=1
            else:
                if k==j+1:
                    x=1
                break
        if x==1:
            break

print(co)
