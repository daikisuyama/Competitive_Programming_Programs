def main():
    import sys
    from collections import Counter
    input=sys.stdin.readline
    n=int(input())
    b=list(map(int,input().split()))
    a=Counter(b)
    ans=0
    for k in b:
        divisors=[]
        for i in range(1,int(k**0.5)+1):
            if k%i==0:
                divisors.append(i)
                if i!=k//i:
                    divisors.append(k//i)
        for j in divisors:
            if (j in a and j!=k)or(j==k and a[j]>1):
                break
        else:
            ans+=1
    print(ans)

if __name__ == '__main__':
    main()