n=int(input())
s=[int(i) for i in input()]

def my_index(l,x,ind):
    '''
    l-イテラブルなオブジェクト
    x-探したい値
    ind-探し始めたいインデックス
    返り値-存在する場合はそのインデックス、存在しない場合は-1
    '''
    global n
    if ind==n:
        return -1
    for i in range(ind,n):
        if l[i]==x:
            return i
    else:
        return -1

c=0
for i in range(10):
    x1=my_index(s,i,0)
    if x1!=-1:
        for j in range(10):
            x2=my_index(s,j,x1+1)
            if x2!=-1:
                for k in range(10):
                    if my_index(s,k,x2+1)!=-1:
                        c+=1
print(c)
