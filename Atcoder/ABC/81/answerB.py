n=int(input())
a=list(map(int,input().split()))
ans=0
def check_all():
    global a,n
    for i in range(n):
        if a[i]%2!=0:
            return False
    return True
while check_all():
    ans+=1
    for i in range(n):
        a[i]//=2
print(ans)
