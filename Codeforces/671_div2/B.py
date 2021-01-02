cand=[1]
for i in range(50):
    cand.append(cand[-1]*2+1)
    if cand[-1]>10**18:
        break
print(cand[30-1]*(cand[30-1]+1)//2)
for i in range(int(input())):
    ans=0
    x=int(input())
    for i in cand:
        j=i*(i+1)//2
        if x-j<0:
            break
        else:
            x-=j
            ans+=1
    print(ans)
