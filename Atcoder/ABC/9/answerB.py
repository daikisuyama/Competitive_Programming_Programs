n=int(input())
a=sorted(set([int(input())for i in range(n)]),reverse=True)
print(a[1])
