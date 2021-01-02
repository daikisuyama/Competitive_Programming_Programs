h=int(input())
cnt=0
while True:
    h=h//2
    cnt+=1
    if h==0:
        break
print(2**cnt-1)
