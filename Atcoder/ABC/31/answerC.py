n=int(input())
a=[int(i) for i in input().split()]

def aoki(s):
    re=0
    l=len(s)
    for i in range(l):
        if i%2==1:
            re+=s[i]
    return re

def takahashi(s):
    re=0
    l=len(s)
    for i in range(l):
        if i%2==0:
            re+=s[i]
    return re

ma=[]
for i in range(n):
    ma_sub1=-1000000000000#aoki
    ma_sub2=-1000000000000#takahashi
    for j in range(n):
        if i==j:
            continue
        elif i>j:
            if aoki(a[j:i+1])>ma_sub1:
                ma_sub1=aoki(a[j:i+1])
                ma_sub2=takahashi(a[j:i+1])
        else:
            if aoki(a[i:j+1])>ma_sub1:
                ma_sub1=aoki(a[i:j+1])
                ma_sub2=takahashi(a[i:j+1])
    ma.append(ma_sub2)
print(max(ma))
