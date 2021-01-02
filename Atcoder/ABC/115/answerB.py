n=int(input())
p=[int(input()) for i in range(n)]
p.sort()
print(sum(p)-p[-1]//2)