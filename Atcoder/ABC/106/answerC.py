s=input()
k=int(input())
l=0
for i in s:
    if i=="1":
        l+=1
    else:
        break
print("1" if k<=l else s[l])
