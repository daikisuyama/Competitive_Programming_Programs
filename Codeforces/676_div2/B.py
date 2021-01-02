for _ in range(int(input())):
    n=int(input())
    s=[input() for i in range(n)]
    f1=[int(s[0][1]),int(s[1][0])]
    f2=[int(s[-1][-2]),int(s[-2][-1])]
    ans=[]
    if f1==[0,0]:
        if f2[0]==0:
            ans.append([n,n-1])
        if f2[1]==0:
            ans.append([n-1,n])
    elif f1==[1,1]:
        if f2[0]==1:
            ans.append([n,n-1])
        if f2[1]==1:
            ans.append([n-1,n])
    elif f2==[0,0]:
        if f1[0]==0:
            ans.append([1,2])
        if f1[1]==0:
            ans.append([2,1])
    elif f2==[1,1]:
        if f1[0]==1:
            ans.append([1,2])
        if f1[1]==1:
            ans.append([2,1])
    elif f1==[0,1] or f1==[1,0]:
        if f1==[0,1]:
            ans.append([2,1])
        else:
            ans.append([1,2])
        if f2[0]==0:
            ans.append([n,n-1])
        if f2[1]==0:
            ans.append([n-1,n])
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1])