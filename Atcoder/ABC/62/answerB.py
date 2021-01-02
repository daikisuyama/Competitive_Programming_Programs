h,w=map(int,input().split())
hw=["#"*(w+2)]
for i in range(h):
    hw.append("#"+input()+"#")
hw.append("#"*(w+2))
for i in range(h+2):
    print(hw[i])
