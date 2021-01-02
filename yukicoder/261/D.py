s=input()
n=len(s)
#dp[i][j]:=i文字目まで決めた時にアルファベットjになるような(文字列の個数,Runの個数)
#ペアにしてもつの珍しいけど、どちらもわからないと決まらないので
#MLEになった
dp=[[[0,0] for i in range(26)] for i in range(n)]
mod=10**9+7
for i in range(n):
    d=ord(s[i])-97
    #新しく追加
    dp[i][d]=[1,1]
    if i==0:continue
    #選ばない場合(増えはしない)
    for j in range(26):
        dp[i][j][0]+=dp[i-1][j][0]
        dp[i][j][0]%=mod
        dp[i][j][1]+=dp[i-1][j][1]
        dp[i][j][1]%=mod
    #選ぶ場合(異なればその文字列数ぶんだけ増える)
    for j in range(26):
        if j==d:
            dp[i][j][0]+=dp[i-1][j][0]
            dp[i][j][0]%=mod
            dp[i][j][1]+=dp[i-1][j][1]
            dp[i][j][1]%=mod
        else:
            dp[i][d][0]+=dp[i-1][j][0]
            dp[i][d][0]%=mod
            dp[i][d][1]+=(dp[i-1][j][0]+dp[i-1][j][1])
            dp[i][d][1]%=mod
ans=0
for j in range(26):
    ans+=dp[n-1][j][1]
    ans%=mod
print(ans)