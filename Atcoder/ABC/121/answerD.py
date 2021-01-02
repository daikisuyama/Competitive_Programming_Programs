import math
import sys
a,b=map(int,input().split())
if b==0:
    print(0)
    sys.exit()
n=math.floor(math.log2(b))+1
ans=[0]*n
form="0"+str(n)+"b"
sa=format(a,form)
sb=format(b,form)
for i in range(n):
    if i==n-1:
        if (b-a+1)%2==0:
            ans[i]=((b-a+1)//2)%2
        else:
            if sa[i]=="1":
                ans[i]=((b-a+1)//2+1)%2
            else:
                ans[i]=((b-a+1)//2)%2
        break
    if sa[i]=="1" and sb[i]=="0":
        s_compa=sa[:i]+"1"*(n-i)
        cmpa=int(s_compa,2)
        ans[i]=(cmpa-a+1)%2
    elif sa[i]=="0" and sb[i]=="1":
        s_compb=sb[:i]+"1"+"0"*(n-i)
        cmpb=int(s_compb,2)
        ans[i]=(b-cmpb+1)%2
    elif sa[i]=="1" and sb[i]=="1":
        s_compa=sa[:i]+"1"*(n-i)
        cmpa=int(s_compa,2)
        s_compb=sb[:i]+"1"+"0"*(n-i)
        cmpb=int(s_compb,2)
        if cmpa>a:#cmpb<b
            ans[i]=((b-cmpb+1)+(cmpa-a+1))%2
        else:
            ans[i]=(b-a+1)%2
cnt=0
for i in range(n):
    cnt+=(ans[i]*2**(n-i-1))
print(cnt)
