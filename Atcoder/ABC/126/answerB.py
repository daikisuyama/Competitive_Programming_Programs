s=input()
cand=["0"+str(i) for i in range(1,10)]+["10","11","12"]
if s[:2] in cand and s[2:] in cand:
    print("AMBIGUOUS")
elif s[:2] in cand:
    print("MMYY")
elif s[2:] in cand:
    print("YYMM")
else:
    print("NA")