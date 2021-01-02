d=int(input())
c=list(map(int,input().split()))
s=[list(map(int,input().split())) for i in range(d)]
def costcalc(t):
    ans=0
    last=[0]*26
    for i in range(d):
        ans+=s[i][t[i]-1]
        last[t[i]-1]=i+1
        for j in range(26):
            ans-=(c[j]*(i+1-last[j]))
        return max(10**6+ans,0)
anss=[[costcalc([j]*d),j+1] for j in range(26)]
anss.sort(reverse=True)
for i in range(d):
    print(anss[0][1])