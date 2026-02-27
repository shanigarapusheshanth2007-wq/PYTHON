s="nana"
y="na"
c=0
if(y in s):
    for j in range(len(s)-len(y)+1):
        for k in range(len(y)):
            #print(k)
            if(y[k]==s[j+k]):
                c=c+1
            if(c==len(y)):
                print("found at ",j)
        c=0
else:
    print(-1)