N=input()
H=[int(i) for i in input().split()]

#len(H)==1は別でOK
for i in range(len(H)-1):
    if H[i] > H[i+1]+1:
        print("No")
        break
    elif H[i] == H[i+1]+1:
        H[i]-=1
    elif i==0:
        H[i]-=1
    elif H[i-1] < H[i]:
        H[i]-=1
else:
    for i in range(len(H)-1):
        if H[i] > H[i+1]:
            print("No")
            break
    else:
        print("Yes")
