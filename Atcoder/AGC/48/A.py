#コーナーケース
for _ in range(int(input())):
    s=input()
    if all(i=="a" for i in s):
        print(-1)
    else:
        n=len(s)
        if "atcoder"<s:
            print(0)
            continue
        for i in range(n):
            if s[i]!="a":
                if s[i]>"t":
                    print(i-1)
                else:
                    print(i)
                break