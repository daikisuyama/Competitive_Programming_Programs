x=["Re","Do","La","So","Fa"]
s=input()
i=s.index("WBWBWB")
if i==0:
    print("Fa")
elif i==1:
    print("Mi")
elif 2<=i<=5:
    print(x[(i-2)//2])
elif i==6:
    print("Si")
else:#i=7~11
    print(x[(i-3)//2])
