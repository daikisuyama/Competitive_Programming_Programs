from fractions import Fraction
for _ in range(int(input())):
    h,c,t=map(Fraction,input().split())
    if 2*t<=(h+c):
        print(2)
    else:
        #-の単項
        #誤差(Fraction)
        #Decimalは遅い
        #同じとこの処理でもない
        x1=(h-t)//(2*t-h-c)
        x2=x1+1
        x1,x2=Fraction(x1),Fraction(x2)
        y1,y2=Fraction(h*(x1+1)+c*x1)/Fraction(2*x1+1),Fraction(h*(x2+1)+c*x2)/Fraction(2*x2+1)
        if abs(y1-t)<=abs(y2-t):
            print(2*x1+1)
        else:
            print(2*x2+1)