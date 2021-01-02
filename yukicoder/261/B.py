n=int(input())
ans=[]
st=2
if n==1:exit(print(1))
for i in range(n):
    now=[(st+i)%n if st+i!=n else n for i in range(n)][::-1]
    st+=2
    st%=n
    if st==0:st=n
    print(" ".join(map(str,now)))