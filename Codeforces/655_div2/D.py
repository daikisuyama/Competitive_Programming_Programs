#サイクルで2連続で削除できない
n=int(input())
a=list(map(int,input().split()))
a0=[a[i] for i in range(n) if i%2==0]
a1=[a[i] for i in range(n) if i%2==1]
a=a0+a1
l=n//2+1
ans=sum(a[:l])
ans_sub=sum(a[:l])
for i in range(n):
    ans_sub-=a[i]
    ans_sub+=a[(i+l)%n]
    ans=max(ans,ans_sub)
print(ans)