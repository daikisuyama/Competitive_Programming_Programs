N=int(input())
dic={}
for i in range(N):
    k="".join(sorted(list(input())))
    if k in dic:
        dic[k]+=1
    else:
        dic[k]=1
c=0
for i in dic.values():
    c += i*(i-1)

print(c//2)
