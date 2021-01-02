for _ in range(int(input())):
    t=input()
    if all(i=="0" for i in t) or all(i=="1" for i in t):
        print(t)
    else:
        print(len(t)*"01")