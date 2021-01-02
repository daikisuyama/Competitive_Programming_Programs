n=int(input())
d={}
for i in range(n):
    s=input()
    if s in d:
        d[s]+=1
    else:
        d[s]=1
print(max(d, key=d.get))
#辞書にmaxを使うと辞書のキーの最大値を取得できる
#keyに指定した関数を適用したものを比較する
#https://note.nkmk.me/python-dict-value-max-min/
