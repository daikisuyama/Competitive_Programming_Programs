#何も思い浮かばない
#完全に負けた死にたいわかんない
#やっぱりDPだけど式が全く立てれない
#頭悪すぎしね
#移り方考えればそうなるだろうが
#部分文字列〜みたいなので単純にBIT累積和尺取りあたりが使えないとDPで前から決めてくパターンは結構ある
#しかも3^Qみたいなのもあるし

mod=10**9+7
s=input()
l=len(s)
dp=[[0]*4 for i in range(l)]
for i in range(l):
    if i==0:
        dp[i][3]=1
        if s[i]=="A":
            dp[i][0]=1
        elif s[i]=="?":
            dp[i][0]=1
            dp[i][3]=3
    else:
        if s[i]=="A":
            dp[i]=[(dp[i-1][0]+dp[i-1][3])%mod,dp[i-1][1],dp[i-1][2],dp[i-1][3]]
        elif s[i]=="B":
            dp[i]=[dp[i-1][0],(dp[i-1][0]+dp[i-1][1])%mod,dp[i-1][2],dp[i-1][3]]
        elif s[i]=="C":
            dp[i]=[dp[i-1][0],dp[i-1][1],(dp[i-1][1]+dp[i-1][2])%mod,dp[i-1][3]]
        else:
            dp[i]=[(3*dp[i-1][0]+dp[i-1][3])%mod,(3*dp[i-1][1]+dp[i-1][0])%mod,(3*dp[i-1][2]+dp[i-1][1])%mod,(3*dp[i-1][3])%mod]
print(dp[-1][2])