n=int(input())
tree=[[] for i in range(n)]
for i in range(n-1):
    u,v=map(int,input().split())
    tree[u-1].append(v-1)
    tree[v-1].append(u-1)
if n==2:
    print("YES")
    exit()
#nが4以上
for i in range(n):
    if len(tree[i])==2:
        print("NO")
        break
else:
    print("YES")