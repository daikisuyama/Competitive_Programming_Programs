x=["A","G","C","T"]
ans=0
now=0
for i in input():
    if i in x:
        now+=1
    else:
        now=0
    ans=max(now,ans)
print(ans)
