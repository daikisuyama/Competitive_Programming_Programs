s=input()
l=len(s)
for i in range(1,l//2):
    k=(l-i*2)
    if s[:k//2]==s[k//2:k]:
        print(k)
        break
