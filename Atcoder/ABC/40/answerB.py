#n-1以下になるのは確実
#1→nまで増やせばいいし、なんなら半分でいいやん
import math

n=int(input())
least=n-1
for i in range(1,int(math.sqrt(n))+1):
    l=n//i-i+n%i
    if l<least:
        least=l

print(least)
