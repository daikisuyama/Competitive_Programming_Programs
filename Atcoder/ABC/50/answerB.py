n=int(input())
t1=[int(_) for _ in input().split()]
m=int(input())
t2=[]
for i in range(m):
    s=input().split()
    t2.append(sum(t1)-t1[int(s[0])-1]+int(s[1]))
for i in range(m):
    print(t2[i])
