import math
#from scipy.special import comb
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def groupby(a):
    a2=[[a[0],1]]
    for i in range(1,len(a)):
        if a2[-1][0]==a[i]:
            a2[-1][1]+=1
        else:
            a2.append([a[i],1])
    return a2

N,A,B=map(int,input().split())
v=[int(i) for i in input().split()]
v.sort(reverse=True)
v=groupby(v)

if A<=v[0][1]:
    #こっちが間違ってる
    m=min(v[0][1],B)
    co=0
    for i in range(A,m+1):
        #え、虚無なんだけど
        co+=combinations_count(v[0][1],i)
    print(v[0][0])
    print(co)
else:
    al=0
    l=len(v)
    C=0
    for i in range(l):
        C+=v[i][1]
        if C<=A:
            al+=(v[i][0]*v[i][1])
        else:
            C-=v[i][1]
            al+=(v[i][0]*(A-C))
            k=combinations_count(v[i][1],A-C)
            #break忘れてたし
            break
    print(al/A)
    print(k)
