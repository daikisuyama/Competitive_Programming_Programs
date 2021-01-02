#再帰で下から取ってくる重要
n=int(input())
b=[[] for i in range(n)]
for i in range(n-1):
    x=int(input())
    b[x-1].append(i+1)

#
def calc_sal(i):#なんばんめの要素か
    global n,b
    l=len(b[i])
    if l==0:
        return 1
    else:
        m=[]
        for j in range(l):
            m.append(calc_sal(b[i][j]))
        return min(m)+max(m)+1
print(calc_sal(0))
