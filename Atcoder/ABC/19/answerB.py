s1=input()

s2=""
j=0
i=0
for i in range(len(s1)):
    if s1[j]==s1[i]:
        pass
    else:
        s2=s2+s1[j]+str(i-j)
        j=i
#始めと終わりのイメージ

print(s2+s1[j]+str(i-j+1))
#ここだけ1がつく

#抽象化
