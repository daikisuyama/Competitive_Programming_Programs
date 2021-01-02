s=[input() for i in range(3)]
l=[len(s[i]) for i in range(3)]
abc=[0,0,0]
now=0
while abc[now]!=l[now]:
    s_sub=s[now][abc[now]]
    abc[now]+=1
    now=(0 if s_sub=="a" else 1 if s_sub=="b" else 2)
print("A" if now==0 else "B" if now==1 else "C")