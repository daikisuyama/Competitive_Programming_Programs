N=int(input())
W1=input().split()
W2=[]
for i in range(N):
    W2.append(int(W1[i]))
for i in range(N):
    if i==0 or x>abs(sum(W2[i+1:])-sum(W2[:i+1])):
        x=abs(sum(W2[i+1:])-sum(W2[:i+1]))
    else:
        break
print(x)
