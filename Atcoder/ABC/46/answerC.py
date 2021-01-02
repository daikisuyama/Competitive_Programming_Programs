n=int(input())
nt,na=map(int,input().split())
for i in range(n-1):
    t,a=map(int,input().split())
    x=-min((-nt)//t,(-na)//a)
    nt,na=x*t,x*a
print(nt+na)