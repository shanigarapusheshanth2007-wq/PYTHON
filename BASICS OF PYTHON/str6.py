s="f11"
y="b23"
z=-1
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if(s[i]==s[j]):
            if(y[i]==y[j]):
                print("ok continue")
                z=1
            else:
                print("break bro")
                break
                z=0
print(z)