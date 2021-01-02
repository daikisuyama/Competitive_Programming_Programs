from fractions import Fraction
n=int(input())
a=[Fraction(input()) for i in range(n)]
c=[a[i].denominator for i in range(n)]
print(c)