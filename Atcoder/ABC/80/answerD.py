#区間スケジューリングでやろうとしたけどチャンネルのカウントが面倒そう？？
n,c=map(int,input().split())
st=[]
for i in range(n):
    s,t,_c=map(int,input().split())
    st.append((s-0.5,t))
st.sort(key=lambda x: x[1])
check=[0]*n
