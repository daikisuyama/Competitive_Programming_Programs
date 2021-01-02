x=[0]*6
for i in input():
    if i=="A":
        x[0]+=1
    elif i=="B":
        x[1]+=1
    elif i=="C":
        x[2]+=1
    elif i=="D":
        x[3]+=1
    elif i=="E":
        x[4]+=1
    else:
        x[5]+=1
print(" ".join(list(map(str,x))))
