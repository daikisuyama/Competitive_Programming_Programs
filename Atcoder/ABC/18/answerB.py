s=list(input())
n=int(input())
for i in range(n):
    l,r=input().split()
    l,r=int(l)-1,int(r)-1
    ss=""
    for j in range(r-l+1):
        ss+=s[r-j]
    s[l:r+1]=list(ss)
#逆順はs[::-1]でもOK
#文字列化はjoin
print("".join(s))
#文字列イミュータブル
