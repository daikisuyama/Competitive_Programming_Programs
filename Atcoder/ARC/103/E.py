s=input()
n=len(s)
if s[n-1]=="1" or s[n-2]=="0" or s[0]=="0":
    print(-1)
else:
    for i in range(n-1):
        if s[i]!=s[n-i-2]:
            print(-1)
            exit()
    #0,n-2は必ず1
    ans=[]
    #どこから伸ばすか
    #きた！
    now=1
    #n//2までしか見なくて良いのか(n-1まで見りゃええやん)
    for i in range(n-1):
        if s[i]=="1":
            ans.append([now,i+2])
            now=i+2
        else:
            ans.append([now,i+2])
    for i in ans:
        print(i[0],i[1])