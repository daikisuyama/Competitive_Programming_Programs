a=int(input())
b=int(input())
if a%b==0:
    print(0)
else:
    print((a//b+1)*b-a)
