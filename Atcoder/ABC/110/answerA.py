abc=list(map(int,input().split()))
abc.sort(reverse=True)
print(int(str(abc[0])+str(abc[1]))+abc[2])