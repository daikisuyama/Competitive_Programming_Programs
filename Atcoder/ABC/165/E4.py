def main():
    n,m=map(int,input().split())
    if n%2==1:
        x=[f"{i+1} {n-i}" for i in range(m)]
        print(" ".join(x))
    else:
        x=[f"{i+1} {n-i}" if i<m/2 else f"{i+1} {n-i-1}" for i in range(m)]
        print(" ".join(x))

if __name__ == "__main__":
    main()