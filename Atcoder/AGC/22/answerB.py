n=int(input())
arrange=[]
ans3=[[3]]
ans2=[[2]]
for i in range(2,30001):
    if i%6==0:
        arrange.append(i)
for i in range(4,30001):
    if i%6!=0 and i%3==0:
        if len(ans3[-1])==2:
            ans3.append([i])
        else:
            ans3[-1].append(i)
for i in range(3,30001):
    if i%6!=0 and i%2==0:
        if len(ans2[-1])==2:
            ans2.append([i])
        else:
            ans2[-1].append(i)
if n==3:
    print("2 5 63")
    exit()
ans=ans2[0]+ans3[0]
ans2.pop(0)
ans3.pop(0)
n-=4
if n==0:
    print(" ".join(map(str,ans)))
    exit()
if n==1:
    ans.append(6)
    print(" ".join(map(str,ans)))
    exit()
for i in ans3:
    n-=2
    ans.append(i[0])
    ans.append(i[1])
    if n>1:
        continue
    elif n==0:
        print(" ".join(map(str,ans)))
        exit()
    else:
        ans.append(arrange[0])
        print(" ".join(map(str,ans)))
        exit()
for i in ans2:
    n-=2
    ans.append(i[0])
    ans.append(i[1])
    if n>1:
        continue
    elif n==0:
        print(" ".join(map(str,ans)))
        exit()
    else:
        ans.append(arrange[0])
        print(" ".join(map(str,ans)))
        exit()
for i in arrange:
    n-=1
    ans.append(i)
    if n==0:
        print(" ".join(map(str,ans)))
        exit()