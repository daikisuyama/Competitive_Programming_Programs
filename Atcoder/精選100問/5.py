#11/25 8:28~8:32
a,b,c,x,y=map(int,input().split())
#a,bを別に買うか,abで買って残りを揃えるか
#多く買いすぎるのも良い
print(min([a*x+b*y,2*c*min(x,y)+((y-x)*b if x<y else (x-y)*a),2*c*max(x,y)]))