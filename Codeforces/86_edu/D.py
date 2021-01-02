n,k=map(int,input().split())
m=sorted(list(map(int,input().split())),reverse=True)
c=list(map(int,input().split()))
ans=[[m[0]]]
#ansの長さ
l=1
#どのansの配列に入れられるか(更新に注意)(空いているように)
now=0
for i in range(1,n):
    if c[m[i-1]-1]<c[m[i]-1]:
        now=0
        ans[now].append(m[i])
    else:
        while now!=l:
            if len(ans[now])<c[m[i]-1]:
                break
            now+=1
        if now==l:
            ans.append([m[i]])
            l+=1
        else:
            ans[now].append(m[i])
print(len(ans))
for i in range(len(ans)):
    print(len(ans[i]),end=" ")
    print(" ".join(map(str,ans[i])))