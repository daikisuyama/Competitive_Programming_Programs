def groupby(a):
    a2=[[a[0],1]]
    for i in range(1,len(a)):
        if a2[-1][0]==a[i]:
            a2[-1][1]+=1
        else:
            a2.append([a[i],1])
    return a2
s1=list(input())
l=len(s1)
s2=groupby(s1)
now=0
for i in s2:
    now+=i[1]
    if i[1]!=1:
        print(str(now-i[1]+1)+" "+str(now))
        break
else:
    if l==2:
        print("-1 -1")
    else:
        for i in range(l-2):
            if s1[i]==s1[i+2]:
                print(str(i+1)+" "+str(i+3))
                break
        else:
            print("-1 -1")
