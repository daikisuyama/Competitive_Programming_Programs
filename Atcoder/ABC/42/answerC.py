n,k=map(int,input().split())
s=set(input().split())
while True:
    l=list(str(n))
    for i in l:
        if i in s:
            break
    else:
        break
    n+=1
print(n)
