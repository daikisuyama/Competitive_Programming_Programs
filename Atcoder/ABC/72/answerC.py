import bisect
n=int(input())
a=sorted([int(i) for i in input().split()])

ma=0
for i in range(10**5):
    ma=max(bisect.bisect_right(a,i+1)-bisect.bisect_left(a,i-1),ma)
print(ma)
#累積和でやると早い
