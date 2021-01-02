def groupby(a):
    a2=[[a[0],1]]
    for i in range(1,len(a)):
        if a2[-1][0]==a[i]:
            a2[-1][1]+=1
        else:
            a2.append([a[i],1])
    return a2
w=list(input())
w.sort()
w=groupby(w)
for i in w:
    if i[1]%2==1:
        print("No")
        break
else:
    print("Yes")