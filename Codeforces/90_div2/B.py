for _ in range(int(input())):
    s=input()
    print(["NET","DA"][min(s.count("1"),s.count("0"))%2])