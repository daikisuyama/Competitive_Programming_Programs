for _ in range(int(input())):
    n=int(input())
    ans=[]
    i=1
    while i<n:
        if len(ans)!=0:
            if ans[-1]==n//i:
                break
        ans.append(n//i)
        i+=1
    if len(ans)==0:
        print(2)
        print("0 1")
        continue
    for i in range(ans[-1]-1,-1,-1):
        ans.append(i)
    print(len(ans))
    print(" ".join(map(str,ans[::-1])))