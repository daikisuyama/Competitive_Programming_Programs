d,d_=dict(),dict()
s,t=input(),input()
l=len(s)
for i in range(l):
    if s[i] not in d:
        d[s[i]]=[i]
    else:
        d[s[i]].append(i)
for i in range(l):
    if t[i] not in d_:
        d_[t[i]]=[i]
    else:
        d_[t[i]].append(i)
x=[sorted(i[1]) for i in list(d.items())]
y=[sorted(i[1]) for i in list(d_.items())]
x.sort()
y.sort()
print(d)
print(d_)
print("Yes" if x==y else "No")