n=int(input())
s=[int(input())for i in range(n)]
s.sort()
def groupby(a):
    a2=[[a[0],1]]
    for i in range(1,len(a)):
        if a2[-1][0]==a[i]:
            a2[-1][1]+=1
        else:
            a2.append([a[i],1])
    return a2
s=groupby(s)
l=len(s)
cnt=0
for i in range(l):
    cnt+=s[i][1]%2
print(cnt)
