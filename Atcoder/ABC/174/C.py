k=int(input())
now=7%k
if now==0:
    print(1)
    exit()
for i in range(1,k):
    now=10*now+7
    now%=k
    if now==0:
        print(i+1)
        break
else:
    print(-1)