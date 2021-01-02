n=int(input())
d={"AC":0,"WA":0,"TLE":0,"RE":0}
for i in range(n):
    d[input()]+=1
print("AC x "+str(d["AC"]))
print("WA x "+str(d["WA"]))
print("TLE x "+str(d["TLE"]))
print("RE x "+str(d["RE"]))