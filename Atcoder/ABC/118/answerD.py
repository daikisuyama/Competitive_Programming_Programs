n,m=map(int,input().split())
x=[2,5,5,4,5,6,3,7,6]
a=[]
for i in map(int,input().split()):
    a.append([i,x[i-1]])
mi=a[0]
for i in range(1,m):
    if mi[1]>a[i][1] or (mi[1]==a[i][1] and a[i][0]>mi[0]):
        mi=a[i]
a=[a[i] for i in range(m) if a[i][0]>=mi[0]]
m=len(a)
b=sorted(a,key=lambda x:x[1])
c=sorted(a,reverse=True)#最後にmi
d1=n//mi[1]#桁数
ans=[mi[0]]*d1
d2=n%mi[1]#後使えるのはどれくらいか
now=0#ansのどこを変えようとしているのか
for i in range(m-1):
    y=d2//(c[i][1]-mi[1])
    if y!=0:
        for j in range(now,now+y):
            ans[j]=c[i][0]
        now+=y
        d2-=(c[i][1]-mi[1])*y
    if d2==0:
        break
cnt=0
for i in range(d1):
    cnt=cnt*10+ans[i]
print(cnt)