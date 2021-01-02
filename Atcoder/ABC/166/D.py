x=int(input())
for A in range(10**3):
    k=A**5-x
    if k>=0:
        l=int(k**0.2)
        if l**5==k:
            print(A,l)
            break
    else:
        k=-k
        l=int(k**0.2)
        if l**5==k:
            print(A,-l)
            break

