N=int(input())
P1=input().split()
P2=[]
for i in range(N):
    P2.append(int(P1[i]))

co=0
for i in range(N):
    if P2[i]!=i+1:
        co+=1
        if co>1:
            print("NO")
            break
        j=P2.index(i+1)
        k=P2[i]
        P2[i]=P2[j]
        P2[j]=k
    if i==N-1:
        print("Yes")
