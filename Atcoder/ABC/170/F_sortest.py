from collections import*
v,a=range,print
h,r,*b=open(0)
h,w,k,r,s,t,u=map(int,(h+a).split())
l=[[-1]*w for _ in v(h)]
l[r][s]=0
d=deque([(r,s)])
while d:
  x,y=d.popleft();j=l[x][y]
  if(x==t)&(y==u):exit(a(j))
  for e,f in[[1,0],[-1,0],[0,-1],[0,1]]:
    for i in v(1,k+1):
      p,q=x+e*i,y+f*i
      if not((0<=p<h)&(0<=q<w))or b[p][q]=="@" or 0<=l[p][q]<=j:break
      if l[p][q]<0:d+=[(p,q)];l[p][q]=j+1
a(-1)