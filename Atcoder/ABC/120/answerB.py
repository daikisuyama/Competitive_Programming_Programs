a,b,k=input().split()
a,b,k=int(a),int(b),int(k)
c=0
for i in range(min(a,b)):
    if a%(min(a,b)-i)==0 and b%(min(a,b)-i)==0:
        #print(i+1)
        c+=1
    if c==k:
        print(min(a,b)-i)
        break

#大きいと小さいを逆だと思っていた
