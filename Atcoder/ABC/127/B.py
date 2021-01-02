r,d,x=map(int,input().split())
ans=[x]
for i in range(10):
    ans.append(r*ans[-1]-d)
for i in range(1,11):
    print(ans[i])