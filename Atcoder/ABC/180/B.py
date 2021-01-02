n=input()
x=list(map(lambda y:abs(int(y)),input().split()))
print(sum(x),sum([i*i for i in x])**0.5,max(x))