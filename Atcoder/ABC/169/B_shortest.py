t=1;print([t:=(-1,t:=t*int(a))[0<=t<=1e18]for a in[*open(0)][1].split()][-1])