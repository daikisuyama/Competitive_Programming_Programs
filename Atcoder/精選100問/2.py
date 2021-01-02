#11/25 8:13~8:16
def make_divisors(n):
    divisors=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            divisors.append(i)
            if i!=n//i:
                divisors.append(n//i)
    return divisors
print(sum([len(make_divisors(i+1))==8 and (i+1)%2 for i in range(int(input()))]))