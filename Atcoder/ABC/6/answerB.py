n=int(input())
a1=0
a2=0
a3=1
if n==1 or n==2:
    print(0)
elif n==3:
    print(1)
else:
    for i in range(n-3):
        a0=a1
        a1=a2
        a2=a3
        a3=(a0+a1+a2)%10007
    print(a3%10007)
#大きな桁は先にあまり出す
