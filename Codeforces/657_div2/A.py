#abacaのできる可能性のあるところにチェック
#おかしい
#インデックスミスなど…
a=["a","b","a","c","a","b","a"]
t=int(input())
for _ in range(t):
    n=int(input())
    s=list(input())
    check=[0]*(n-6)            
    for i in range(n-6):
        for j in range(i,i+7):
            if s[j]!=a[j-i] and s[j]!="?":
                break
        else:
            if s[i:i+7]==a:
                check[i]=2
            else:
                check[i]=1
    if check.count(2)>1:
        print("No")
        continue
    elif check.count(2)==1:
        print("Yes")
        print(("".join(s)).replace("?","z"))
        continue
    #?を変えて一個だけのパターン
    g=False
    for i in range(n-6):
        if check[i]==1:
            f=False
            cand=[a[j-i] if i<=j<=i+6 else s[j] if s[j]!="?" else "z" for j in range(n)]
            for j in range(n-6):
                if i!=j:
                    for k in range(j,j+7):
                        if cand[k]!=a[k-j]:
                            break
                    else:
                        f=True
            if not f:
                print("Yes")
                print("".join(cand))
                g=True
                break
    if not g:print("No")