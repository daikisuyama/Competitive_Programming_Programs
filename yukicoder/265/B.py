#2,5以外の約数あるか
from math import gcd
a,b=map(int,input().split())
b//=gcd(a,b)
while b%2==0:
    b//=2
while b%5==0:
    b//=5
print(["Yes","No"][b==1])