#問題文を見直せ
#一つだけWAのパターンは特殊パターン

s=input()
k=int(input())

if k<=len(s):
    x=[]
    for i in range(len(s)-k+1):
        if s[i:i+k] not in x:
            x.append(s[i:i+k])
    print(len(x))
else:
    print(0)
