n,k,c=map(int,input().split())
s=input()
#働く日のうちi日目についてそれ以後でないと働けない日をL[i]とする配列を考える
#働く日のうちi日目についてそれ以前でないと働けない日をR[i]とする配列も考える
#その二つが同じとき、必ず働かなければいけない日になる
#L[i]があった時、L[i]+c+1以降からしか働けないことに注意(vice versa)


l=[-1]*k
r=[-1]*k
nowl=0
indl=0
while nowl<n and indl<k:
    for i in range(nowl,n):
        if s[i]=="o":
            l[indl]=i
            nowl=i+c+1
            indl+=1
            break
nowr=n-1
indr=k-1
while nowr>=0 and indr>=0:
    for i in range(nowr,-1,-1):
        if s[i]=="o":
            r[indr]=i
            nowr=i-c-1
            indr-=1
            break
for i in range(k):
    if l[i]==r[i]:
        print(l[i]+1)