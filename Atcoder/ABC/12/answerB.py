n=int(input())
h=n//(60**2)
if h<10:
    h="0"+str(h)
else:
    h=str(h)
m=(n%(60**2))//60
if m<10:
    m="0"+str(m)
else:
    m=str(m)
s=(n%(60**2))%60
if s<10:
    s="0"+str(s)
else:
    s=str(s)

#print(f"{h}:{m}:{s}")
#3.6より前なので
print("{}:{}:{}".format(h,m,s))
