n=int(input())
s=input()


if n%2==0:
    print(-1)
elif n==1:
    if s=="b":
        print(0)
    else:
        print(-1)
else:#3以上の奇数の時
    for i in range((n-1)//2):
        k1=(n-1)//2-i-1
        k2=(n-1)//2+i+1
        if i%3==2:
            if s[k1]=="b" and s[k2]=="b":
                pass
            else:
                print(-1)
                break
        else:
            if s[k1] in ["a","c"] and s[k2] in ["a","c"]:
                pass
            else:
                print(-1)
                break
    #1の時はelseの文を実行してしまうので、else文使わない方がいいかも
    else:
        print(i+1)
