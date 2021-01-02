n=int(input())
a,b=input().split()
a,b=int(a),int(b)
k=int(input())
p=[int(i) for i in input().split()]
p.append(a)
p.append(b)
if len(p)!=len(set(p)):
    print("NO")
else:
    print("YES")
#for文の中でappendは避ける
