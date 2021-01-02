for i in range(int(input())):
    n=int(input())
    s=input()
    if all([i=="1" for i in s]) or all([i=="0" for i in s]):
        print(s)
        continue
    #l,r必ずある
    l,r=-1,n
    for i in range(n):
        if s[i]=="1":
            l=i
            break
    for i in range(n-1,-1,-1):
        if s[i]=="0":
            r=i
            break
    if l>r:
        print(s)
        continue
    print(s[:l]+"0"+s[r+1:])