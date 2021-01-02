a,b=input().split()
sa,sb=sum(int(i) for i in a),sum(int(i) for i in b)
print(sa if sa>sb else sb)