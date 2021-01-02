s=input()
from itertools import groupby
print(max([0]+[len(list(g)) for k,g in groupby(s,key=lambda x:x in "ACGT")if k]))