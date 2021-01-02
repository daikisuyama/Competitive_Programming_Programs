#余りごとで見ていく

#題意を全て勘違いしていた
#一回だけだと思っていた
n,k=map(int,input().split())
a=list(map(int,input()))
ans=[-1]*n
upper=False
lower=False
#lowerとupperで更新起きるじゃんかす
#更新は起きていいんか、ダメでしょ
for i in range(k):
    ans[i]=a[i]
for i in range(k,n):
    ans[i]=ans[i-k]
    if ans[i]==a[i]:
        pass
    elif ans[i]>a[i]:
        #先にupperとなる場合
        #変えなくて大丈夫
        if lower==False and upper==False:
            upper=True
    else:
        #先にlowerとなる場合
        #lowerのとこを変えるだけ
        #変えると超えるか
        if lower==False and upper==False:
            lower=True
            #一番したのやつを変える
            #9だとだめ
            #それより下は0にする
            for j in range(k-1,-1,-1):
                if ans[j]!=9:
                    break
            for l in range(i+1):
                if l%k==j:
                    ans[l]+=1
                elif l%k>j:
                    ans[l]=0

print(n)
print("".join(map(str,ans)))