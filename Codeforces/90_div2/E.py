for _ in range(int(input())):
    n,k=map(int,input().split())
    ans=[]
    #繰り上がりない
    if n<=(18-k)*(k+1)//2:
        for i in range(10):
            check=n
            for j in range(k+1):
                if i+j>9:
                    break
                else:
                    check-=(i+j)
            else:
                if check==0:
                    ans.append(i)
    else:
        check=n-(18-k)*(k+1)//2
        if check%(k+1)==0:
            check//=(k+1)
            i,j=check%9,check//9
            if i==0:
                ans.append(int("9"*j+f"{9-k}"))
            else:
                ans.append(int(f"{i}"+"9"*j+f"{9-k}"))
    #繰り上がりある
    for num9 in range(20):
        for j in range(k):
            check=n-(18-j)*(j+1)//2-(k-j)*(k-j-1)//2
            check-=(num9*9*(j+1))
            check-=(1*(k-j))
            #print(check)
            if check>=0:
                if check%(k+1)==0:
                    check//=(k+1)
                    h,i=check%9,check//9
                    #9で割れる必要はない
                    if i==0:
                        if h==0:
                            ans.append(int("9"*num9+f"{9-j}"))
                        else:
                            ans.append(int(f"{h}"+"9"*num9+f"{9-j}"))
                    else:
                        check-=8
                        h,i=check%9,check//9
                        if h==0:
                            ans.append(int("9"*i+"8"+"9"*num9+f"{9-j}"))
                        else:
                            ans.append(int(f"{h}"+"9"*i+"8"+"9"*num9+f"{9-j}"))
    #print(ans)
    if len(ans):
        print(min(ans))
    else:
        print(-1)

