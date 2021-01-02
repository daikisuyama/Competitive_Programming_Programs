import sys
input=sys.stdin.readline
for _ in range(int(input())):
    s=input()
    n=len(s)
    check=[0]*n
    ans=[]
    for i in range(n):
        if s[i:i+5]=="twone":
            ans.append(str(i+3))
            for j in range(i,i+5):
                check[j]=1
    for i in range(n):
        if check[i]:
            continue
        if s[i:i+3]=="one":
            ans.append(str(i+2))
        if s[i:i+3]=="two":
            ans.append(str(i+2))
    print(s.count("one")+s.count("two")-s.count("twone"))
    print(" ".join(ans))