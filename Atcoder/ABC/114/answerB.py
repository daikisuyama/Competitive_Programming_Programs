s=input()
l=len(s)
ans=[]
for i in range(l-3+1):
    ans.append(abs(int(s[i:i+3])-753))
print(min(ans))