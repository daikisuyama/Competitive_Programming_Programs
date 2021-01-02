n=int(input())

if n==2:
    print(-1)
else:
    x=[]
    if n%3==0:
        for i in range(n//3):
            x.append("."*(3*i)+"a"+"."*(n-3*i-1))
            x.append("."*(3*i)+"a"+"."*(n-3*i-1))
            x.append("."*(3*i)+".aa"+"."*(n-3*i-3))
    elif n%6==1:
        for i in range(n//6-1):
            x.append("."*(6*i)+".a.b.c"+"."*(n-6*i-6))
            x.append("."*(6*i)+".a.b.c"+"."*(n-6*i-6))
            x.append("."*(6*i)+"ddg.ll"+"."*(n-6*i-6))
            x.append("."*(6*i)+"e.g.kk"+"."*(n-6*i-6))
            x.append("."*(6*i)+"e.hhj."+"."*(n-6*i-6))
            x.append("."*(6*i)+"ffiij."+"."*(n-6*i-6))
        x.append("."*(n-7)+".aab.c.")
        x.append("."*(n-7)+"d..b.c.")
        x.append("."*(n-7)+"d..eeff")
        x.append("."*(n-7)+"g..mm.l")
        x.append("."*(n-7)+"gnn...l")
        x.append("."*(n-7)+"h...kkj")
        x.append("."*(n-7)+"hii...j")
    elif n%6==2:
        for i in range(n//6-1):
            x.append("."*(6*i)+".a.b.c"+"."*(n-6*i-6))
            x.append("."*(6*i)+".a.b.c"+"."*(n-6*i-6))
            x.append("."*(6*i)+"ddg.ll"+"."*(n-6*i-6))
            x.append("."*(6*i)+"e.g.kk"+"."*(n-6*i-6))
            x.append("."*(6*i)+"e.hhj."+"."*(n-6*i-6))
            x.append("."*(6*i)+"ffiij."+"."*(n-6*i-6))
        x.append("."*(n-8)+".a.bb.cc")
        x.append("."*(n-8)+".a...m.j")
        x.append("."*(n-8)+"..pp.m.j")
        x.append("."*(n-8)+"hh..i.o.")
        x.append("."*(n-8)+"gg..i.o.")
        x.append("."*(n-8)+"..n.ll.k")
        x.append("."*(n-8)+"f.n....k")
        x.append("."*(n-8)+"f.dd.ee.")
    elif n%6==4:
        for i in range(n//6):
            x.append("."*(6*i)+".a.b.c"+"."*(n-6*i-6))
            x.append("."*(6*i)+".a.b.c"+"."*(n-6*i-6))
            x.append("."*(6*i)+"ddg.ll"+"."*(n-6*i-6))
            x.append("."*(6*i)+"e.g.kk"+"."*(n-6*i-6))
            x.append("."*(6*i)+"e.hhj."+"."*(n-6*i-6))
            x.append("."*(6*i)+"ffiij."+"."*(n-6*i-6))
        x.append("."*(n-4)+"aacb")
        x.append("."*(n-4)+"ffcb")
        x.append("."*(n-4)+"hgdd")
        x.append("."*(n-4)+"hgee")
    else:
        for i in range(n//6):
            x.append("."*(6*i)+".a.b.c"+"."*(n-6*i-6))
            x.append("."*(6*i)+".a.b.c"+"."*(n-6*i-6))
            x.append("."*(6*i)+"ddg.ll"+"."*(n-6*i-6))
            x.append("."*(6*i)+"e.g.kk"+"."*(n-6*i-6))
            x.append("."*(6*i)+"e.hhj."+"."*(n-6*i-6))
            x.append("."*(6*i)+"ffiij."+"."*(n-6*i-6))
        x.append("."*(n-5)+"aabbc")
        x.append("."*(n-5)+"g.h.c")
        x.append("."*(n-5)+"gjh..")
        x.append("."*(n-5)+"dj.ii")
        x.append("."*(n-5)+"deeff")
    for i in range(n):
        print("".join(x[i]))

#また出力が違うやつをやりましたが
