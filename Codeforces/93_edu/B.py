for _ in range(int(input())):
    s=input()
    n=len(s)
    ans=[0]
    for i in range(n):
        if s[i]=="1":
            ans[-1]+=1
        else:
            if ans[-1]!=0:
                ans.append(0)
    ans.sort(reverse=True)
    print(sum(ans[::2]))