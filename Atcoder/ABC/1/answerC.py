d,s=map(int,input().split())
for i,j in enumerate([0,3,16,34,55,80,108,139,172,208,245,285,327]):
    if s/6+0.5001>=j:w=i
print("{} {}".format("N NNE NE ENE E ESE SE SSE S SSW SW WSW W WNW NW NNW N".split()[int(d/225+0.5)],w) if w else "C 0")