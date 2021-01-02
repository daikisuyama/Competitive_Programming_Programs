s=input()
ans=1
l=len(s)
now=s[0]
i=1
while i<l:
    if now!=s[i]:
        now=s[i]
        ans+=1
        i+=1
    else:
        if len(now)==2:
            now=s[i]
            ans+=1
            i+=1
        else:
            if i<l-1:
                now=s[i:i+2]
                i+=2
                ans+=1
            else:
                break
    #print(i)
print(ans)