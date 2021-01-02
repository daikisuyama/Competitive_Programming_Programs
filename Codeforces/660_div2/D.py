from collections import deque
ans=0
n=int(input())
a=list(map(int,input().split()))
b=[i-1 if i!=-1 else -1 for i in list(map(int,input().split()))]
flow=[0]*n
graph=[[] for i in range(n)]
for i in range(n):
    if b[i]!=-1:
        flow[b[i]]+=1
        graph[i].append(b[i])
check=[a[i] for i in range(n)]
ver=deque()
lv=0
for i in range(n):
    if flow[i]==0:
        ver.append(i)
        lv+=1
f,s=[],[]
while lv:
    #print(ver)
    for i in range(lv):
        x=ver.popleft()
        lv-=1
        if check[x]>=0:
            f.append(x)
            for j in graph[x]:
                flow[j]-=1
                check[j]+=check[x]
                if flow[j]==0:
                    ver.append(j)
                    lv+=1
        else:
            s.append(x)
            for j in graph[x]:
                flow[j]-=1
                if flow[j]==0:
                    ver.append(j)
                    lv+=1
#print(check)
print(sum(check))
print(" ".join(map(lambda x:str(x+1),f+s[::-1])))