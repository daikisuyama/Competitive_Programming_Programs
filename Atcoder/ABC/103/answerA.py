a,b,c=map(int,input().split())
print(min(abs(b-a)+abs(a-c),abs(b-c)+abs(c-a),abs(a-b)+abs(b-c)))