S=input()
a="Good"

for i in range(3):
    if S[i]== S[i+1]:
        a="Bad"
        break
print(a)
