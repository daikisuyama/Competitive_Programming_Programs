n=int(input())
def groupby(a):
    a2=[[a[0],1]]
    for i in range(1,len(a)):
        if a2[-1][0]==a[i]:
            a2[-1][1]+=1
        else:
            a2.append([a[i],1])
    return a2

b=groupby(sorted([int(i) for i in input().split()]))
l=len(b)
co=0
for i in range(l):
    co+=(b[i][1]-1)
if co%2==0:
    print(l)
else:
    print(l-1)
