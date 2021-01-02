x=int(input())
ans=[1]
for i in range(2,x+1):
    k=2
    while True:
        a=i**k
        if a<=x:
            ans.append(a)
            k+=1
        else:
            break
print(max(ans))