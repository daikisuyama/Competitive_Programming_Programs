import math
n=int(input())
a1,a2,a3,a4=[],[],[],[]

for i in range(n):
    x,y=map(int,input().split())
    if x>0 and y>0:
        a1.append((x,y))
    elif x>0 and y<0:
        a2.append((x,y))
    elif x<0 and y<0:
        a3.append((x,y))
    elif x<0 and y>0:
        a4.append((x,y))
    elif x==0 and y>0:
        a1.append((x,y))
        a4.append((x,y))
    elif x==0 and y<0:
        a2.append((x,y))
        a3.append((x,y))
    elif x>0 and y==0:
        a1.append((x,y))
        a2.append((x,y))
    elif x<0 and y==0:
        a3.append((x,y))
        a4.append((x,y))

s=[[0,0],[0,0],[0,0],[0,0]]
#print(s)
#print(a1)
#print(a2)
#print(a3)
#print(a4)

def ze(v):
    return math.sqrt(v[0]**2+v[1]**2)

for i in a1:
    s[0][0]+=i[0]
    s[0][1]+=i[1]
for i in a2:
    s[1][0]+=i[0]
    s[1][1]+=i[1]
for i in a3:
    s[2][0]+=i[0]
    s[2][1]+=i[1]
for i in a4:
    s[3][0]+=i[0]
    s[3][1]+=i[1]

#傾きで場合分け
#時間内ではここまで

if mai==0:
    a=[a2,a4]
elif mai==1:
    a=[a1,a3]
elif mai==2:
    a=[a2,a4]
else:
    a=[a3,a1]

p=s[mai]






print(max(list(map(ze,s))))
#j=0
#ma=s[j][0]**2+s[j][1]**2
#for i in range(1,4):
#    if s[i][0]**2+s[i][1]**2>ma:
#        j=i
#        ma=s[i][0]**2+s[i][1]**2
