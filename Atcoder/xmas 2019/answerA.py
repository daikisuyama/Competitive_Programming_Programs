import numpy as np
from PIL import Image
im = np.array(Image.open('signboard_t1/design.png').convert('L').resize((256, 256)))
th = 128
im_bin_128 = (im > th) * 255
#print(len(im_bin_128))
#print(len(im_bin_128[0]))

'''
file = open('Out2.txt', 'w')
for i in range(256):
    file.write(" ".join(list(map(str,im_bin_128[i])))+"\n")
file.close()
'''

a=[["." for i in range(256)] for j in range(256)]
for i in range(256):
    for j in range(256):
        if im_bin_128[i][j]<=1:
            a[i][j]="#"

'''
l=0
for i in range(8):
    for j in range(8):
        l+=1
        file = open('fuck/Out{}.txt'.format(l), 'w')
        for k in range(32):
            file.write("".join(a[i*32+k][j*32:j*32+32])+"\n")
        file.close()
'''
def all_sor(x,y):
    c=0
    for i in range(32):
        for j in range(32):
            if x[i][j]==y[i][j]:
                c+=1
    return c



ans=[[0 for i in range(8)] for j in range(8)]
liness=[]

for i in range(64):
    f=open("signboard_t1/pieces/{}.txt".format(i+1))
    lines=list(map(list,[s.strip() for s in f.readlines()]))
    #print(lines)
    f.close()
    liness.append(lines)

for j in range(8):
    for k in range(8):
        b,c=j*32,k*32
        x=[[a[ji][ki] for ki in range(c,c+32)] for ji in range(b,b+32)]
        ma=[0,0]
        for i in range(64):
            if all_sor(x,liness[i])>ma[1]:
                ma=[i,all_sor(x,liness[i])]
        ans[j][k]=ma[0]


for i in range(8):
    print(" ".join(map(str,ans[i])))
