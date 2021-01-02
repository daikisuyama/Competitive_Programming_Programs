visited=[0]
visited_set=set()
visited_set.add(0)
n,k=map(int,input().split())
a=list(map(int,input().split()))
next1=0
next2=-1
while True:
    next2=a[next1]-1
    next1=next2
    if next2 in visited_set:
        break
    else:
        visited.append(next2)
        visited_set.add(next2)
#print(visited)
if k<len(visited):
    print(visited[k]+1)
else:
    loop_len=(len(visited)-visited.index(next2))
    k-=(len(visited)-loop_len)
    print(visited[k%loop_len+visited.index(next2)]+1)