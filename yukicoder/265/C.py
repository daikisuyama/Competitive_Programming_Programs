n=int(input())
s=list(map(int,input().split()))
t=list(map(int,input().split()))
if s.count(2)>0 and t.count(2):
    print(s.count(2)*n+t.count(2)*n-s.count(2)*t.count(2))
elif s.count(2)>0:
    print(s.count(2)*n+s.count(1))
elif t.count(2)>0:
    print(t.count(2)*n+t.count(1))
else:
    print(max(s.count(1),t.count(1)))