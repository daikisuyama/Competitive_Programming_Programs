from math import gcd
for _ in range(int(input())):
    a,b=map(int,input().split())
    if gcd(a,b)==1:
        print("Finite")
    else:
        print("Infinite")