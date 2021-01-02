n=int(input())
s=input().split()
a=[[int(s[i]),i+1] for i in range(n)]
a.sort(key=lambda x:x[0],reverse=True)
for i in range(n):
    print(a[i][1])
