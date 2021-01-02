from math import gcd
def lcm(a,b):
    return a//gcd(a,b)*b
x=int(input())
print(lcm(360,x)//x)