#こういう問題で実際に動かすやつはあほ、普通にチェンジするとこまで行って、どっちか(偶数だけ離れてるとこ)に集まるやろ
s=input()
n=len(s)
#変わる点というより変わる点にくる集まりを考えるべき
d=0
a=[]
ax=[0]

for i in range(n):
    l=len(ax)
    if l==1:
        if s[i]=="L":
            ax.append(i-1)
            ax.append(i)
        if i==n-1:
            ax.append(i)
            a.append(ax)
    elif l==3:
        if s[i]=="R":
            ax.append(i-1)
            a.append(ax)
            ax=[i]
        elif i==n-1:
            ax.append(i)
            a.append(ax)
m=len(a)
c=[0]*n
for i in range(m):
    #print(type(a[i][1]))
    #print(type(c[a[i][1]]))
    c[a[i][1]]=(a[i][1]-a[i][0])//2+(a[i][3]-a[i][1])//2+1
    c[a[i][2]]=(a[i][2]-a[i][0])//2+(a[i][3]-a[i][2])//2+1

print(" ".join(list(map(str,c))))
