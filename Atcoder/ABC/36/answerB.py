from collections import deque

n=int(input())
d=[deque() for i in range(n)]
for i in range(n):
    s=input()
    for j in range(n):
        d[j].appendleft(s[j])

for i in range(n):
    for j in range(n):
        print(d[i][j],end="")
    print()
