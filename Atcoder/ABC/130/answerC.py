#中心以外は完全な対称性を持っていないので、二つ以上引いても対称にならない
w,h,x,y=[int(i) for i in input().split()]
print(w*h/2,end=" ")
if w==x*2 and h==y*2:
    print(1)
else:
    print(0)
