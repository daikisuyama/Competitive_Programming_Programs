#11/25 9:40~9:53
#高速化: 20ふん
#2本決めればいける
def main():
    n=int(input())
    points=[tuple(map(int,input().split())) for i in range(n)]
    p=set(points)
    ans=0
    for i in range(n):
        x1,y1=points[i]
        for j in range(i+1,n):
            x2,y2=points[j]
            ch=[y1-y2,x2-x1]
            if (x1+ch[0],y1+ch[1]) in p and (x2+ch[0],y2+ch[1]) in p:
                ans=max(ans,(y1-y2)**2+(x2-x1)**2)
                continue
            ch=[y2-y1,x1-x2]
            if (x1+ch[0],y1+ch[1]) in p and (x2+ch[0],y2+ch[1]) in p:
                ans=max(ans,(y1-y2)**2+(x2-x1)**2)
    print(ans)
main()