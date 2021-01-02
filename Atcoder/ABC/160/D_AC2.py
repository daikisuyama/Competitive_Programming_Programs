#そもそもO(N^2)の意識がなかった
#無理やり最短距離を求めようとして数え忘れたパターンがあった
#このパターンはしっかりサンプル見て実験していれば避けれていた
#自分の考察に自信を持つ姿勢はいいけど、詰まったら疑って実験する
n,x,y=map(int,input().split())
ans=[[1000000]*n for i in range(n)]
for i in range(n-1):
    for j in range(i+1,n):
        ans[i][j]=min(j-i,abs(x-1-i)+1+abs(y-1-j))
_ans=[0]*(n-1)
for i in range(n-1):
    for j in range(i+1,n):
        _ans[ans[i][j]-1]+=1
for i in range(n-1):
    print(_ans[i])
