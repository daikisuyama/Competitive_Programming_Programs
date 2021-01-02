#誤読(出力するものミス)
t=int(input())
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    for i in range(1,n-1):
        if p[i-1]<p[i] and p[i]>p[i+1]:
            print("Yes")
            print(i,i+1,i+2)
            break
    else:
        print("No")