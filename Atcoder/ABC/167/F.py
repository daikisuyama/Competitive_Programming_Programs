import sys
n=int(input())
s=[input() for i in range(n)]
t=[2*(i.count("("))-len(i) for i in s]
if sum(t)!=0:
    print("No")
    sys.exit()
st=[[t[i]] for i in range(n)]

for i in range(n):
    now,mi=0,0
    for j in s[i]:
        if j=="(":
            now+=1
        else:
            now-=1
        mi=min(mi,now)
    st[i].append(mi)
#st.sort(reverse=True,key=lambda z:z[1])
u,v,w=list(filter(lambda x:x[1]>=0,st)),list(filter(lambda x:x[1]<0 and x[0]>=0,st)),list(filter(lambda x:x[1]<0 and x[0]<0,st))
v.sort(reverse=True)
v.sort(reverse=True,key=lambda z:z[1])
w.sort(key=lambda z:z[0]-z[1],reverse=True)
lu=len(u)
lv=len(v)
now2=0
for i in range(n):
    if i<lu:
        now2+=u[i][0]
    elif i<lu+lv:
        if now2+v[i-lu][1]<0:
            print("No")
            break
        now2+=v[i-lu][0]
    else:
        #いや、間違ってるのここなんかーーい
        if now2+w[i-lu-lv][1]<0:
            print("No")
            break
        now2+=w[i-lu-lv][0]
else:
    print("Yes")