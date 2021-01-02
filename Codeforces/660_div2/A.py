for i in range(int(input())):
    n=int(input())
    if n<=30:
        print("NO")
    elif n==36:
        print("YES")
        print("6 10 15 5")
    elif n==40:
        print("YES")
        print("6 10 15 9")
    elif n==44:
        print("YES")
        print("6 10 15 13")
    else:
        print("YES")
        print("6 10 14"+f" {n-30}")