n=int(input())
P1=input().split()
P2=[]
for i in range(n):
    P2.append(int(P1[i]))

c=0
for i in range(n-2):
    if max(P2[i:i+3])!=P2[i+1] and min(P2[i:i+3])!=P2[i+1]:
        c+=1

print(c)
