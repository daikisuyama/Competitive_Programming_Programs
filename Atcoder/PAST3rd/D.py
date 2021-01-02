n=int(input())
num=["####.##.##.####",".#.##..#..#.###","###..#####..###","###..####..####","#.##.####..#..#","####..###..####","####..####.####","###..#..#..#..#","####.#####.####","####.####..####"]
ans_sub=[""]*n
ans=["0"]*n
for i in range(5):
    s=input()
    for j in range(1,n+1):
        ans_sub[j-1]+=s[4*j-3:4*j]
for i in range(n):
    for j in range(10):
        if ans_sub[i]==num[j]:
            ans[i]=str(j)
            break
print("".join(ans))