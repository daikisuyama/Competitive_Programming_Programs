s=input()
n=len(s)
#dp[i][j]:=i文字目まで決めた時にアルファベットjになるような(文字列の個数,Runの個数)
#ペアにしてもつの珍しいけど、どちらもわからないと決まらないので
#MLEになった
#dpを配列にしない
x,y=[[0,0] for i in range(26)],[[0,0] for i in range(26)]
mod=10**9+7
for i in range(n):
    d=ord(s[i])-97
    #新しく追加
    if i==0:
        x[d]=[1,1]
        continue
    #選ばない場合(増えはしない)
    for j in range(26):
        y[j][0]=x[j][0]
        y[j][0]%=mod
        y[j][1]=x[j][1]
        y[j][1]%=mod
    y[d][0]+=1
    y[d][1]+=1
    #選ぶ場合(異なればその文字列数ぶんだけ増える)
    for j in range(26):
        if j==d:
            y[j][0]+=x[j][0]
            y[j][0]%=mod
            y[j][1]+=x[j][1]
            y[j][1]%=mod
        else:
            y[d][0]+=x[j][0]
            y[d][0]%=mod
            y[d][1]+=(x[j][0]+x[j][1])
            y[d][1]%=mod
    x,y=y,x
ans=0
for j in range(26):
    ans+=x[j][1]
    ans%=mod
print(ans)