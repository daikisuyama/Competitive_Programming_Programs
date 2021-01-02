#a,b=input().split();print(int(a)*int(b.strip("."))//100)
a,b=input().split();print(int(a)*int(b[:-3]+b[-2:])//100)