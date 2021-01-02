for _ in range(int(input())):
    n,k=map(int,input().split())
    s=[int(i=="(") for i in input()]
    goal=[]
    for i in range(k-1):
        goal.append(1)
        goal.append(0)
    for i in range((n-(k-1)*2)//2):
        goal.append(1)
    for i in range((n-(k-1)*2)//2):
        goal.append(0)
    ans=[]
    for i in range(n):
        if s[i]!=goal[i]:
            for j in range(i+1,n):
                if s[j]==goal[i]:
                    ans.append((str(i+1),str(j+1)))
                    break
            s_sub=s[i:j+1][::-1]
            for k in range(i,j+1):
                s[k]=s_sub[k-i]
    print(len(ans))
    for i in ans:
        print(" ".join(i))