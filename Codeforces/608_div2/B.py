n=int(input())
s=list(input())
ans=[]
if s[0]=="W":
    ans.append(0)
    s[0]="B"
    if s[1]=="W":
        s[1]="B"
    else:
        s[1]="W"
for i in range(1,n-1):
    if s[i]=="W":
        s[i]="B"
        if s[i+1]=="W":
            s[i+1]="B"
        else:
            s[i+1]="W"
        ans.append(i)
if s!=["B" for i in range(n)] and n%2==0:
    print(-1)
    exit()
if s!=["B" for i in range(n)]:
    for i in range(n-1):
        if i%2==0:
            ans.append(i)

print(len(ans))
print(" ".join(map(str,[i+1 for i in ans])))