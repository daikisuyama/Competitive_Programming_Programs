for _ in range(int(input())):
    n=int(input())
    p=list(map(int,input().split()))
    print(" ".join(map(str,p[::-1])))