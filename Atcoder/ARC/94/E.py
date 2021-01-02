n=int(input())
ab=[list(map(int,input().split())) for i in range(n)]
if all(i[0]==i[1] for i in ab):
    print(0)
    exit()
s=sum(i[0] for i in ab)
mi=10**12
for i in range(n):
    if ab[i][0]>ab[i][1]:
        mi=min(mi,ab[i][1])
print(s-mi)