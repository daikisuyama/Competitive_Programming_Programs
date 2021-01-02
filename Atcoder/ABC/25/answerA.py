s=list(input())
n=int(input())
s.sort()
i=(n-1)//5
j=(n-1)%5
print(s[i]+s[j])
