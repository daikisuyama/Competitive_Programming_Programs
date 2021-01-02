from itertools import groupby
s=input()
print(len(list(groupby(s)))-1)