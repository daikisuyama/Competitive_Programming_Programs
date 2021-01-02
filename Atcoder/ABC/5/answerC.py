t=int(input())
n=int(input())
a=[int(i) for i in input().split()]
m=int(input())
b=[int(i) for i in input().split()]

if m>n:
    print("no")
else:
    j=0
    for i in range(n):
        #print(j)
        if a[i]<=b[j]<=a[i]+t:
            a[i]=0
            j+=1
            if j==m:
                print("yes")
                break
    else:
        print("no")
