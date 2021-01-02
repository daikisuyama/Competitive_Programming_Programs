#×最適性
n=int(input())
a=list(map(int,input().split()))
x=sum(a)//4
p,sp=0,0
for i in range(n):
    sp+=a[i]
    p=i
    if sp>=x:
        break

def qq(p_):
    global n,a
    x=(sum(a)-sum(a[:p_+1]))//3
    q_,sq_=0,0
    for i in range(p_+1,n):
        sq_+=a[i]
        q_=i
        if sq_>=x:
            break
    return [q_-1,q_]
def rr(q_):
    global n,a
    x=(sum(a)-sum(a[:q_+1]))//2
    r_,sr_=0,0
    for i in range(q_+1,n):
        sr_+=a[i]
        r_=i
        if sr_>=x:
            break
    return [r_-1,r_]
f=[p-1,p] if p!=0 else [p]
ans=[]
for z1 in f:
    for z2 in qq(z1):
        for z3 in rr(z2):
            cand=[sum(a[:z1+1]),sum(a[z1+1:z2+1]),sum(a[z2+1:z3+1]),sum(a[z3+1:])]
            ans.append(max(cand)-min(cand))
print(min(ans))


