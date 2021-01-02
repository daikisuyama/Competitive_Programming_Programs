from itertools import groupby
s=input()
ans=[key+str(len(list(group))) for key,group in groupby(s)]
print("".join(ans))