def main():
    from sys import exit
    s=input()
    x,y=map(int,input().split())

    def groupby(a):
        a2=[[a[0],1]]
        for i in range(1,len(a)):
            if a2[-1][0]==a[i]:
                a2[-1][1]+=1
            else:
                a2.append([a[i],1])
        return a2

    s=groupby(s)
    a,b=[],[]
    turn=True
    #初めまっすぐの場合
    if s[0][0]=="F":
        x-=s[0][1]
        s.pop(0)
    for i in s:
        if i[0]=="F":
            if turn:
                a.append(-i[1])
            else:
                b.append(-i[1])
        elif i[1]%2==1:
            turn=not turn
    a.sort()
    b.sort()
    for i in a:
        x=abs(x)-abs(i)
    if x!=0:
        print("No")
        exit()
    for i in b:
        y=abs(y)-abs(i)
    if y!=0:
        print("No")
        exit()
    print("Yes")
main()

    