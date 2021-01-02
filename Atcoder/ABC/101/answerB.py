n1=int(input())
#数字列を数値の配列に直す(一旦、イテラブルな文字列を経由することで簡単に書ける)
n2=[int(x) for x in str(n1)]
if n1%sum(n2)==0:
    print("Yes")
else:
    print("No")
