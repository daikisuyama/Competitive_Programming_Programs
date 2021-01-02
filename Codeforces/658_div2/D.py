t=int(input())
for _ in range(t):
    n=int(input())
    a,b=input(),input()
    dif=[i+1 for i in range(n) if a[i]!=b[i]]
    if dif==[]:
        print(0)
        continue
    if len(dif)==1:
        if dif[0]==1:
            print("1 1")
        elif dif[0]==n:
            print(f"2 {n-1} {n}")
        else:
            print(f"4 {dif[0]} {n-dif[0]+1} {dif[0]-1} {n-dif[0]}")
        continue
    #ここまででdifは2より大きい
    #入れ替えると前は必ず1ではなくなる
    #nになるのは構わない
    dif[0],dif[1]=dif[1],dif[0]
    #ansl,ansrは必ず1差になるように
    l=len(dif)
    if dif[-1]==n:l-=1
    ansl,ansr=[],[]
    for i in range(l):
        if i%2==0:
            ansl.append(dif[i])
            ansl.append(dif[i]-1)
        else:
            ansr.append(n-dif[i]+1)
            ansr.append(n-dif[i])
    if dif[-1]==n:
        if l%2==0:
            ansl.append(n-1)
            ansr.append(n)
        else:
            ansr.append(1)
    else:
        if l%2==0:
            pass
        else:
            ansr.append(n)
            ansr.append(n)
    l=len(ansr)
    ans=[]
    for i in range(l):
        ans.append(ansl[i])
        ans.append(ansr[i])
    if len(ansl)>len(ansr):
        ans.append(ansl[-1])
    print(str(len(ans))+" "+" ".join(map(str,ans)))

