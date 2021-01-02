sx,sy,tx,ty=map(int,input().split())
path1=(tx-sx)*"R"+(ty-sy)*"U"
path2=(tx-sx)*"L"+(ty-sy)*"D"
path3="D"+(tx-sx+1)*"R"+(ty-sy+1)*"U"+"L"
path4="U"+(tx-sx+1)*"L"+(ty-sy+1)*"D"+"R"
print(path1+path2+path3+path4)
