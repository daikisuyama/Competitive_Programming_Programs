n,x=input().split()
#xを二進数表記に直す
n,x=int(n),format(int(x),"b")
c=0
a=input().split()
for i in range(len(x)):
    if x[-i-1]=="1":
        c+=int(a[i])
print(c)

#https://note.nkmk.me/python-bin-oct-hex-int-format/
#https://webkaru.net/clang/decimal-to-binary/
