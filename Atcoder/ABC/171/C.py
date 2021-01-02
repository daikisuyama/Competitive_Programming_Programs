n=int(input())-1
def n_len():
    global n
    i=1
    while n>=26**i:
        n-=26**i
        i+=1
    return i
l=n_len()
alp=[chr(i) for i in range(97, 97+26)]
ans=""
for i in range(l):
    k=n%26
    ans=alp[k]+ans
    n//=26
print(ans)