a,b,c=input().split()
a,b,c=int(a),int(b),int(c)
k=(a*b)%(10**9+7)
print((k*c)%(10**9+7))
#計算量減らせてる?
#桁数減ってるし
#時間計りたい
